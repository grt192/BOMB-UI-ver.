from PySide6.QtWidgets import (
    QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout, QApplication, QLabel,
    QSlider)
from Widgets.BaseLabels.DoubleLabel import DoubleLabel
from Widgets.MotorControlWidget.SliderWidget import SliderWidget
from Widgets.MotorControlWidget.SpeedIndexWidget import SpeedIndexWidget
from PySide6.QtCore import Qt
import sys
from Widgets.MotorControlWidget.MotorStatsWidget import MotorStatsWidget


class SpeedControlWidget(QWidget):
    def __init__(self, motorID, isLocal, parent = None):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.motorID = motorID
        self.targetSpeed = None

        self.layout = QVBoxLayout()

        self.sliderWidget = SliderWidget(motorID, isLocal)
        self.layout.addWidget(self.sliderWidget)

        self.speedIndexWidget = SpeedIndexWidget(self)
        self.layout.addWidget(self.speedIndexWidget)

        self.speedLabel = DoubleLabel(motorID + "Speed", isLocal)

        self.setLayout(self.layout)

        self.speedIndexWidget.newSpeedSignal.connect(self.setSlider)

    def setMotorID(self, motorID: int):
        self.motorID = motorID

    def setTargetSpeed(self, targetSpeed: float):
        self.targetSpeed = targetSpeed

    def setSlider(self, value):
        self.sliderWidget.slider.setValue(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeedControlWidget("1", True)
    window.show()
    # window.setGeometry(0, 0, 1920, 780)
    app.exec()