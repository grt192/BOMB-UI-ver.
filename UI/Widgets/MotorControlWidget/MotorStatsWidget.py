from PySide6.QtWidgets import (
    QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout, QApplication, QLabel,
    QSlider)
from Widgets.BaseLabels.DoubleLabel import DoubleLabel
from PySide6.QtCore import Qt

import sys


class MotorStatsWidget(QWidget):
    def __init__(self, motorID, isLocal, parent = None):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMaximumHeight(100)

        self.motorID = motorID
        self.targetSpeed = None

        self.layout = QHBoxLayout()

        self.idLabel = QLabel(motorID)
        self.idLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.idLabel)
        self.currentLabel = DoubleLabel(motorID + "Current", isLocal, self)
        self.layout.addWidget(self.currentLabel)
        self.voltageLabel = DoubleLabel(motorID + "Voltage", isLocal, self)
        self.layout.addWidget(self.voltageLabel)
        self.temperatureLabel = DoubleLabel(motorID + "Temp", isLocal, self)
        self.layout.addWidget(self.temperatureLabel)

        self.setLayout(self.layout)

    def update(self, motorID, isLocal):
        self.currentLabel.update(self.motorID + "Current", isLocal)
        self.voltageLabel.bindNTManager(self.motorID + "Voltage", isLocal)
        self.temperatureLabel.bindNTManager(self.motorID + "Temp", isLocal)

    def setMotorID(self, motorID: int):
        self.motorID = motorID

    def setTargetSpeed(self, targetSpeed: float):
        self.targetSpeed = targetSpeed


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MotorStatsWidget("1", True)
    window.show()
    # window.setGeometry(0, 0, 1920, 780)
    app.exec()

