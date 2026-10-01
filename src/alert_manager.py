import time
import winsound

class AlertManager:
    def __init__(self, cooldown_seconds=3):
        self.cooldown = cooldown_seconds
        self.last_alert = 0

    def alert(self):
        now = time.time()
        if now - self.last_alert >= self.cooldown:
            winsound.Beep(1000, 800)
            self.last_alert = now
