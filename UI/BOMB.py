import sys
# PySide6 imports
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QSlider
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt, Slot
from Widgets.MotorControlWidget.MotorControlWidget import MotorControlWidget

class BOMB(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("BOMB (UI ver.)")
        self.resize(1920, 1080)
        self.mainLayout = QHBoxLayout()

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.mainLayout)

        # self.motorStack1 = QVBoxLayout()
        # self.motorStack2 = QVBoxLayout()
        #
        self.stack1 = QVBoxLayout()
        self.stack2 = QVBoxLayout()
        self.motorWidget1 = MotorControlWidget("1", False)
        self.motorWidget2 = MotorControlWidget("2", False)
        self.motorWidget3 = MotorControlWidget("3", False)
        self.motorWidget4 = MotorControlWidget("4", False)
        self.stack1.addWidget(self.motorWidget1)
        self.stack1.addWidget(self.motorWidget2)
        self.stack2.addWidget(self.motorWidget3)
        self.stack2.addWidget(self.motorWidget4)

        self.mainLayout.addLayout(self.stack1)
        self.mainLayout.addLayout(self.stack2)

        # self.motorStack1.addWidget(self.motorWidget1)
        #
        # self.motorWidget2 = MotorControlWidget()
        # self.motorStack1.addWidget(self.motorWidget2)
        #
        # self.motorWidget3 = MotorControlWidget()
        # self.motorStack2.addWidget(self.motorWidget3)
        #
        # self.motorWidget4 = MotorControlWidget()
        # self.motorStack2.addWidget(self.motorWidget4)
        #
        # self.mainLayout.addLayout(self.motorStack1)
        # self.mainLayout.addLayout(self.motorStack2)

        # self.slider1 = QSlider(Qt.Horizontal)
        # self.slider1.setRange(-1, 1)
        # self.slider1.setSingleStep(0.02)
        # # self.slider1.setPageStep(0.1)
        # self.slider1.setValue(0)
        # self.slider1.valueChanged.connect(self.on_slider_value_changed)
        # self.mainLayout.addWidget(self.slider1)
        # self.setStyleSheet("background-color: black; color: white;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BOMB()
    window.show()
    # window.setGeometry(0, 0, 1920, 780)
    app.exec()