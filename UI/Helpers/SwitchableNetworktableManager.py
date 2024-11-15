from networktables import NetworkTables
from PySide6.QtCore import Signal, QObject
import time
from Constants import Constants
class SwitchableNetworkTableManager(QObject):

    newValueAvailable = Signal(tuple)

    def __init__(self, entryName, isLocal, parent=None):
        super().__init__(parent)

        if isLocal:
            self.setLocal()
        else:
            self.setRio()

        self.connectNT(entryName)

    def connectNT(self, entryName: str):
        self.table = NetworkTables.getTable(Constants.ROOT_TABLE_NAME)
        print("connecting" + entryName)
        if self.table is None:
            print("Table not found")
            return
        self.entry = self.table.getEntry(entryName)
        if self.entry is None:
            print("Entry not found")
            return
        self.entry.addListener(
            self.valueChanged,
            NetworkTables.NotifyFlags.UPDATE |
            NetworkTables.NotifyFlags.LOCAL
        )

    def valueChanged(self, table, key, value, isNew):
        # print("value: " + str(value))
        self.newValueAvailable.emit((key, value))

    def getValue(self):
        if self.table is None:
            return None
        return self.table.getValue(self.entryName, None)

    def putDouble(self, value):
        if self.entry is None:
            print("Entry not found")
            return
        print("putting nt" + str(value))
        self.entry.setDouble(value)

    def setLocal(self):
        NetworkTables.initialize(server='localhost')

    def setRio(self):
        NetworkTables.initialize(server='10.1.92.2')