from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Spam Detector")

        button = QPushButton('Click me!')
        self.setCentralWidget(button)
        button.setCheckable(True)
        button.setChecked(True)

    def click_button(self) -> None:
        print('Clicked!')

    def toggle_button(self, checked) -> None:
        print('Checked: ', checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()