from gui import SpamDetector
from train import train_model
from utils import get_model

import sys
from PySide6.QtWidgets import QApplication

if get_model().exists():
    train_model()

app = QApplication(sys.argv)
window = SpamDetector()
window.show()

app.exec()