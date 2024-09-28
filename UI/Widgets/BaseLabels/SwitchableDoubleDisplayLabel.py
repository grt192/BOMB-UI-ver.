from PySide6.QtWidgets import  QLabel
from PySide6.QtCore import Qt
from Helpers.SwitchableNetworktableManager import SwitchableNetworkTableManager


class SwitchableDoubleDisplayLabel(QLabel):

  def __init__(
    self, tableName: str = None, entryName: str = None, parent = None):
    super().__init__(parent)

    self.tableName = tableName
    self.entryName = entryName

    self.setStyleSheet(f"background-color: gray;")
    self.setText("No Data")

    self.setAlignment(Qt.AlignCenter)
    self.setAutoFillBackground(True)
    self.NTManager = SwitchableNetworkTableManager()

  def bindNTManager(self, tableName: str, entryName: str):
    self.NTManager.connect(tableName, entryName) 
    self.NTManager.newValueAvailable.connect(self.updateFromNT)

  def updateFromNT(self, message: tuple):
    self.setText(self.parameterName + str(float(message[1])))
    self.setStyleSheet(f"background-color: black; color: red;")