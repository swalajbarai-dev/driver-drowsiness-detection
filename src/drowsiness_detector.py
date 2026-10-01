class DrowsinessDetector:
    def __init__(self, threshold_frames=45):
        self.threshold_frames = threshold_frames
        self.closed_frames = 0

    def update(self, eye_count):
        if eye_count >= 2:
            self.closed_frames = 0
            return "AWAKE", self.closed_frames

        self.closed_frames += 1
        if self.closed_frames >= self.threshold_frames:
            return "DROWSY", self.closed_frames
        return "CHECKING", self.closed_frames

    def reset(self):
        self.closed_frames = 0
