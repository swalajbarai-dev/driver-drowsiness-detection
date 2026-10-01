from collections import Counter
from pathlib import Path

class SessionStatistics:
    def __init__(self):
        self.counts = Counter()

    def update(self, status):
        self.counts[status] += 1

    def save(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write("Session Summary\n")
            f.write("================\n")
            for key in ["AWAKE", "CHECKING", "DROWSY"]:
                f.write(f"{key}: {self.counts[key]} frames\n")
