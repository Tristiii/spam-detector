from gui import SpamDetector

import sys
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
window = SpamDetector()
window.show()

app.exec()