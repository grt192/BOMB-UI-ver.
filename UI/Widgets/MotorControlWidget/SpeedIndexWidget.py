from PySide6.QtWidgets import (
    QSizePolicy, QWidget, QHBoxLayout, QApplication, QPushButton, QLineEdit
)
from PySide6.QtCore import Signal
import sys


class SpeedIndexWidget(QWidget):
    leftSpeed = 0
    rightSpeed = 0
    newSpeedSignal = Signal(float)

    def __init__(self, parent = None):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QHBoxLayout()

        self.leftApplyButton = QPushButton("Apply")
        self.leftSpeedLineEdit = QLineEdit(self)
        self.zeroLabel = QPushButton("0")
        self.rightSpeedLineEdit = QLineEdit(self)
        self.rightApplyButton = QPushButton("Apply")
        self.layout.addWidget(self.leftApplyButton)
        self.layout.addWidget(self.leftSpeedLineEdit)
        self.layout.addWidget(self.zeroLabel)
        self.layout.addWidget(self.rightSpeedLineEdit)
        self.layout.addWidget(self.rightApplyButton)

        self.leftSpeedLineEdit.textChanged.connect(self.updateLeftIndex)
        self.rightSpeedLineEdit.textChanged.connect(self.updateRightIndex)

        self.leftApplyButton.clicked.connect(self.updateLeftSpeed)
        self.rightApplyButton.clicked.connect(self.updateRightSpeed)
        self.zeroLabel.clicked.connect(self.zeroSpeed)

        self.setLayout(self.layout)

    def updateLeftIndex(self, value):
        try:
            value = int(value)
        except ValueError:
            return

        if abs(value) > 100:
            return

        self.leftSpeed = value
        self.leftApplyButton.setText(str(value))

    def updateRightIndex(self, value):
        try:
            value = int(value)
        except ValueError:
            return

        if abs(value) > 100:
            return
        self.rightSpeed = value
        self.rightApplyButton.setText(str(value))

    def updateLeftSpeed(self):
        self.newSpeedSignal.emit(float(self.leftApplyButton.text()))

    def updateRightSpeed(self):
        self.newSpeedSignal.emit(float(self.rightApplyButton.text()))

    def zeroSpeed(self):
        self.newSpeedSignal.emit(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeedIndexWidget()
    window.show()
    # window.setGeometry(0, 0, 1920, 780)
    app.exec()

