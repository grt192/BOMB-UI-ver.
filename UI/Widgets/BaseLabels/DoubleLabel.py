from PySide6.QtWidgets import  QLabel
from PySide6.QtCore import Qt
from Helpers.SwitchableNetworktableManager import SwitchableNetworkTableManager
from Constants import Constants


class DoubleLabel(QLabel):

    def __init__(self, entryName, isLocal, parent = None):
        super().__init__(parent)

        self.tableName = Constants.ROOT_TABLE_NAME
        self.entryName = entryName

        self.setStyleSheet(f"background-color: gray;")
        self.setText("No Data")

        self.setAlignment(Qt.AlignCenter)
        self.setAutoFillBackground(True)
        self.NTManager = SwitchableNetworkTableManager(entryName, isLocal)
        self.bindNTManager()

    def update(self, entryName, isLocal):
        self.NTManager.connectNT(entryName)
        if(isLocal):
            self.NTManager.setLocal()
        else:
            self.NTManager.setRio()

    def putDouble(self, value):
        self.NTManager.putDouble(value)
    def bindNTManager(self):
        self.NTManager.newValueAvailable.connect(self.updateFromNT)

    def updateFromNT(self, message: tuple):
        self.setText(str(float(message[1])))
        self.setStyleSheet(f"background-color: black; color: red;")