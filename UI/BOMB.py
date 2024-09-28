import sys
# PySide6 imports
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout
from PySide6.QtWidgets import QVBoxLayout
from Widgets.MotorControlWidget import MotorControlWidget

class BOMB(QMainWindow):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("BOMB (UI ver.)")
    self.resize(1000, 1000)
    self.mainLayout = QHBoxLayout()

    self.centralWidget = QWidget(self)
    self.setCentralWidget(self.centralWidget)
    self.centralWidget.setLayout(self.mainLayout)

    self.motorStack1 = QVBoxLayout()
    self.motorStack2 = QVBoxLayout()

    self.motorWidget1 = MotorControlWidget()
    self.motorStack1.addWidget(self.motorWidget1)

    self.motorWidget2 = MotorControlWidget()
    self.motorStack1.addWidget(self.motorWidget2)

    self.motorWidget3 = MotorControlWidget()
    self.motorStack2.addWidget(self.motorWidget3)

    self.motorWidget4 = MotorControlWidget()
    self.motorStack2.addWidget(self.motorWidget4)

    self.mainLayout.addLayout(self.motorStack1)
    self.mainLayout.addLayout(self.motorStack2)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = BOMB()
  window.show()
  # window.setGeometry(0, 0, 1920, 780)
  app.exec()