from src.drowsiness_detector import DrowsinessDetector

def test_awake():
    d = DrowsinessDetector(3)
    assert d.update(2)[0] == "AWAKE"

def test_drowsy_after_threshold():
    d = DrowsinessDetector(3)
    d.update(0)
    d.update(0)
    status, _ = d.update(0)
    assert status == "DROWSY"

def test_reset_after_open_eyes():
    d = DrowsinessDetector(3)
    d.update(0)
    status, frames = d.update(2)
    assert status == "AWAKE"
    assert frames == 0
