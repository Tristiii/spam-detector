from predict import predict_text

import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
)
from PySide6.QtCore import Qt


class SpamDetector(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Spam Detector")
        self.setFixedSize(500, 200)

        layout = QVBoxLayout()

        self.description = QLabel('This spam detector has a accuracy of 95.96%. Please enter your text below.')
        layout.addWidget(self.description)

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Enter a text")
        layout.addWidget(self.text_input)

        self.button = QPushButton('Predict')
        self.button.clicked.connect(self.check_spam)
        layout.addWidget(self.button)

        self.result = QLabel('Please enter a text!')
        self.result.setStyleSheet("""
            background-color: orange;
            color: white;
            font-weight: bold;
            padding: 10px;
        """)
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.result)

        self.setLayout(layout)

    def check_spam(self) -> None:
        message = self.text_input.toPlainText()
        if not message:
            self.result.setText('Please enter a text!')
            self.result.setStyleSheet("""
                background-color: orange;
                color: white;
                font-weight: bold;
                padding: 10px;
            """)
        else:
            prediction = predict_text(message)
            if prediction:
                self.result.setText('SPAM DETECTED!')
                self.result.setStyleSheet("""
                    background-color: red;
                    color: white;
                    font-weight: bold;
                    padding: 10px;
                """)
            else:
                self.result.setText('NOT SPAM!')
                self.result.setStyleSheet("""
                    background-color: green;
                    color: white;
                    font-weight: bold;
                    padding: 10px;
                """)