# Project Report Content

## 1. Introduction
Driver drowsiness is a computer vision application where visual cues such as prolonged eye closure can be monitored from a camera feed. This project implements an academic prototype using Python and OpenCV.

## 2. Problem Statement
Build a real-time system that observes a driver's face and eyes through a webcam and provides an alert when prolonged eye non-detection indicates possible drowsiness.

## 3. Objectives
- Detect a driver's face in real time.
- Detect eyes within the primary face region.
- Monitor consecutive frames with fewer than two detected eyes.
- Generate an audible warning after the configured threshold.
- Store session observations for analysis.

## 4. Functional Requirements
1. Webcam input and frame capture.
2. Face and eye detection.
3. Drowsiness decision.
4. Audible alert.
5. Session logging and statistics.

## 5. Non-Functional Requirements
- Performance: process webcam frames continuously on a normal laptop.
- Reliability: handle webcam access failure and missing faces.
- Maintainability: separate detection, decision, alert, logging and statistics modules.
- Error handling: check camera initialization and frame capture.
- Resource efficiency: process the primary/largest detected face.

## 6. System Architecture
Webcam -> Frame Capture -> Face Detection -> Eye Detection -> Drowsiness Decision -> Alert + Logging -> Session Summary

## 7. Design Decisions
Haar Cascade classifiers were selected because they are available through OpenCV and provide a lightweight, easy-to-demonstrate real-time baseline. A consecutive-frame threshold reduces immediate false alarms from short detection failures.

## 8. Implementation
The implementation is divided into detector, decision, alert, logging and statistics modules. The main controller coordinates these modules.

## 9. Results
During local webcam testing, the system detected the face and both open eyes and displayed AWAKE. When both eyes were kept closed long enough for the configured threshold, the system displayed DROWSY and the warning message, demonstrating the intended prototype behavior.

## 10. Testing
Test cases:
- Webcam unavailable -> error message.
- One detected face -> process primary face.
- Two detected eyes -> AWAKE.
- Temporary eye non-detection -> CHECKING.
- Threshold reached -> DROWSY + alert.
- Quit key -> resources released.
- Unit tests -> drowsiness threshold and reset logic.

## 11. Challenges
Lighting, glasses, head pose and Haar Cascade detection stability can affect eye detection. Threshold selection also affects sensitivity.

## 12. Learnings
The project provided practical experience with image acquisition, grayscale conversion, Haar Cascade detection, frame-based decision logic, modular Python design, logging and testing.

## 13. Future Enhancements
- Facial landmark based Eye Aspect Ratio (EAR)
- PERCLOS-based measurement
- Head-pose estimation
- More robust datasets and evaluation
- Cross-platform alert mechanism
- Dashboard for session analytics

## 14. References
- OpenCV documentation
- Python documentation
