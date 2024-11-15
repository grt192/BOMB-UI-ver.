from PySide6.QtWidgets import (
    QSizePolicy, QWidget, QVBoxLayout, QApplication)
from Widgets.MotorControlWidget.MotorStatsWidget import MotorStatsWidget
from Widgets.MotorControlWidget.SpeedControlWidget import SpeedIndexWidget

import sys

from Widgets.MotorControlWidget.SpeedControlWidget import SpeedControlWidget


class MotorControlWidget(QWidget):
    def __init__(self, motorID, isLocal, parent = None):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.motorID = motorID
        self.targetSpeed = None

        self.layout = QVBoxLayout()

        self.motorStatsWidget = MotorStatsWidget(motorID, isLocal)
        self.layout.addWidget(self.motorStatsWidget)

        self.speedControlWidget = SpeedControlWidget(motorID, isLocal)
        self.layout.addWidget(self.speedControlWidget)

        self.setLayout(self.layout)

    def updateStatsLabels(self):
        self.currentLabel.bindNTManager(self.motorTableName, self.motorID, "C")
        self.voltageLabel.bindNTManager(self.motorTableName, self.motorID, "V")
        self.temperatureLabel.bindNTManager(
            self.motorTableName, self.motorID, "T"
        )

    def setMotorID(self, motorID: int):
        self.motorID = motorID

    def setTargetSpeed(self, targetSpeed: float):
        self.targetSpeed = targetSpeed
  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MotorControlWidget("1", True)
    window.show()
    # window.setGeometry(0, 0, 1920, 780)
    app.exec()

