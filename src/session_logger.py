import csv
from datetime import datetime
from pathlib import Path

class SessionLogger:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.file = open(path, "w", newline="", encoding="utf-8")
        self.writer = csv.writer(self.file)
        self.writer.writerow(["timestamp", "status", "eye_count", "closed_frames"])

    def log(self, status, eye_count, closed_frames):
        self.writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            status, eye_count, closed_frames
        ])
        self.file.flush()

    def close(self):
        self.file.close()
