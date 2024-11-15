from PySide6.QtWidgets import (
    QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout, QApplication, QLabel,
    QSlider)
from Widgets.BaseLabels.DoubleLabel import DoubleLabel
from PySide6.QtCore import Qt
from Widgets.MotorControlWidget.MotorStatsWidget import MotorStatsWidget
import sys


class SliderWidget(QWidget):
    def __init__(self, motorID, isLocal, parent = None):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMaximumHeight(50)

        self.layout = QHBoxLayout()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(100)
        self.slider.setMinimum(-100)
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.updateSpeed)
        self.layout.addWidget(self.slider)

        self.speedLabel = DoubleLabel(motorID + "Speed", isLocal)
        self.layout.addWidget(self.speedLabel)

        self.setLayout(self.layout)

    def updateSpeed(self, value):
        self.speedLabel.putDouble(value)

    def setMotorID(self, motorID: int):
        self.motorID = motorID

    def setTargetSpeed(self, targetSpeed: float):
        self.targetSpeed = targetSpeed

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderWidget("1", True)
    window.show()
    # window.setGeometry(0, 0, 1920, 780)
    app.exec()

