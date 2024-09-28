from PySide6.QtWidgets import QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout
from Widgets.BaseLabels.SwitchableDoubleDisplayLabel import SwitchableDoubleDisplayLabel
from Constants import Constants

class MotorControlWidget(QWidget):

  def __init__(self, parent = None):
    super().__init__()

    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    self.motorID = None
    self.isCTRE = None
    self.targetSpeed = None

    self.layout = QHBoxLayout()

    self.motorStatsStack = QVBoxLayout()

    self.currentLabel = SwitchableDoubleDisplayLabel()
    self.motorStatsStack.addWidget(self.currentLabel)
    self.voltageLabel = SwitchableDoubleDisplayLabel()
    self.temperatureLabel = SwitchableDoubleDisplayLabel()

    self.motorTableName = Constants.MOTOR_TABLE_NAME
  
  def updateStatsLabels(self):
    self.currentLabel.bindNTManager(self.motorTableName, self.motorID, "C")
    self.voltageLabel.bindNTManager(self.motorTableName, self.motorID, "V")
    self.temperatureLabel.bindNTManager(self.motorTableName, self.motorID, "T")

  def setMotorID(self, motorID: int):
    self.motorID = motorID

  def setMotorType(self, isCTRE: bool):
    self.isCTRE = isCTRE
  
  def setTargetSpeed(self, targetSpeed: float):
    self.targetSpeed = targetSpeed
  


