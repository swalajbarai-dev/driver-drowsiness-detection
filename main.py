import cv2

from src.face_detector import FaceDetector
from src.drowsiness_detector import DrowsinessDetector
from src.alert_manager import AlertManager
from src.session_logger import SessionLogger
from src.statistics import SessionStatistics


def main():

    # =====================================================
    # 1. START WEBCAM
    # =====================================================

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("ERROR: Could not access webcam.")
        return

    # =====================================================
    # 2. INITIALIZE PROJECT MODULES
    # =====================================================

    face_detector = FaceDetector()

    drowsiness_detector = DrowsinessDetector(
        threshold_frames=45
    )

    alert_manager = AlertManager(
        cooldown_seconds=3
    )

    logger = SessionLogger(
        "results/drowsiness_log.csv"
    )

    stats = SessionStatistics()

    print("--------------------------------------------")
    print(" DRIVER DROWSINESS DETECTION SYSTEM")
    print("--------------------------------------------")
    print("System started successfully.")
    print("Press 'q' to quit.")
    print("--------------------------------------------")

    # =====================================================
    # 3. MAIN CAMERA LOOP
    # =====================================================

    while True:

        ret, frame = camera.read()

        if not ret:
            print("ERROR: Could not read frame.")
            break

        # -------------------------------------------------
        # Detect faces
        # -------------------------------------------------

        faces = face_detector.detect(frame)

        status = "NO FACE"
        eye_count = 0
        closed_frames = 0

        # IMPORTANT:
        # faces is a NumPy array, so we use len(faces)
        # instead of "if faces"
        if len(faces) > 0:

            # -------------------------------------------------
            # Select largest face
            # -------------------------------------------------

            face = max(
                faces,
                key=lambda r: r[2] * r[3]
            )

            x, y, w, h = face

            # -------------------------------------------------
            # Draw face rectangle
            # -------------------------------------------------

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Face",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            # -------------------------------------------------
            # Detect eyes
            # -------------------------------------------------

            eye_count, eye_boxes = (
                face_detector.detect_eyes(
                    frame,
                    face
                )
            )

            # -------------------------------------------------
            # Draw eye rectangles
            # -------------------------------------------------

            for (ex, ey, ew, eh) in eye_boxes:

                cv2.rectangle(
                    frame,
                    (x + ex, y + ey),
                    (x + ex + ew, y + ey + eh),
                    (255, 0, 0),
                    2
                )

            # -------------------------------------------------
            # Drowsiness detection
            # -------------------------------------------------

            status, closed_frames = (
                drowsiness_detector.update(
                    eye_count
                )
            )

            # -------------------------------------------------
            # Update statistics
            # -------------------------------------------------

            stats.update(status)

            # -------------------------------------------------
            # Save log
            # -------------------------------------------------

            logger.log(
                status,
                eye_count,
                closed_frames
            )

            # -------------------------------------------------
            # Trigger alarm
            # -------------------------------------------------

            if status == "DROWSY":
                alert_manager.alert()

        else:

            # -------------------------------------------------
            # No face detected
            # -------------------------------------------------

            drowsiness_detector.reset()

            status = "NO FACE"
            eye_count = 0
            closed_frames = 0

        # =====================================================
        # 4. DISPLAY INFORMATION
        # =====================================================

        cv2.putText(
            frame,
            f"Eyes: {eye_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Closed frames: {closed_frames}",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        # =====================================================
        # 5. DISPLAY STATUS
        # =====================================================

        if status == "DROWSY":

            status_color = (0, 0, 255)

        elif status == "AWAKE":

            status_color = (0, 255, 0)

        elif status == "CHECKING":

            status_color = (0, 255, 255)

        else:

            status_color = (255, 255, 255)

        cv2.putText(
            frame,
            f"Status: {status}",
            (20, 115),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            status_color,
            2
        )

        # =====================================================
        # 6. DROWSINESS WARNING
        # =====================================================

        if status == "DROWSY":

            cv2.putText(
                frame,
                "WARNING: DROWSINESS DETECTED!",
                (20, 155),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        # =====================================================
        # 7. SHOW CAMERA
        # =====================================================

        cv2.imshow(
            "Driver Drowsiness Detection",
            frame
        )

        # =====================================================
        # 8. QUIT WITH Q
        # =====================================================

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # =====================================================
    # 9. CLEANUP
    # =====================================================

    camera.release()

    cv2.destroyAllWindows()

    logger.close()

    stats.save(
        "results/session_summary.txt"
    )

    print("--------------------------------------------")
    print("Driver Drowsiness Detection stopped.")
    print("Results saved in results/ folder.")
    print("--------------------------------------------")


# =========================================================
# PROGRAM ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()