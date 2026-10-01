# Real-Time Driver Drowsiness Detection and Alert System

## Overview
A Python/OpenCV computer vision prototype that monitors a driver's face and eyes using a webcam. Prolonged absence of both detected eyes is used as a drowsiness indicator, followed by a Windows audible alert and session logging.

## Features
- Real-time webcam processing
- Haar Cascade face detection
- Eye detection within the primary face
- Consecutive-frame drowsiness threshold
- Audible Windows alert with cooldown
- CSV logging
- Session summary
- Automated unit tests for the drowsiness logic

## Technologies
- Python 3.12
- OpenCV
- NumPy
- SciPy
- Pandas
- Pytest

## Installation
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\activate
```

## Run
```powershell
python main.py
```
Press `q` to quit.

## Test
```powershell
pytest -q
```

## Output
After a session, the `results/` folder contains:
- `drowsiness_log.csv`
- `session_summary.txt`

## Method
The system detects the largest face in each frame. Eyes are detected within that face. If fewer than two eyes are detected for the configured number of consecutive frames, the status changes to DROWSY and an audible warning is triggered.

## Limitations
Haar Cascade eye detection can be affected by lighting, glasses, head pose, and occlusion. The prototype should not be treated as a certified driver-safety device.

## Repository Structure
```text
driver-drowsiness-detection/
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── src/
│   ├── face_detector.py
│   ├── drowsiness_detector.py
│   ├── alert_manager.py
│   ├── session_logger.py
│   └── statistics.py
├── tests/
│   └── test_drowsiness.py
├── docs/
└── results/
```
