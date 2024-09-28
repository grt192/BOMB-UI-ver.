from networktables import NetworkTables
from PySide6.QtCore import Signal, QObject
import time
class SwitchableNetworkTableManager(QObject):

  def __init__(
    self, tableName = None, entryName = None, local = False, parent = None):
    super().__init__(parent)

    if local:
      NetworkTables.initialize(server='localhost')
    else:
      NetworkTables.initialize(server='10.1.92.2')

    """
    print("Connecting to " + tableName + "-> " + entryName + ":")
    while not NetworkTables.isConnected():
        print("#", end="")
        time.sleep(0.2)

    print("Connected!")
    """
    self.tableName = tableName
    self.entryName = entryName
    self.table = None
    self.entry = None
    self.newValueAvailable = Signal(tuple)

  def connect(self, tableName: str, entryName: str):
    self.table = NetworkTables.getTable(tableName)
    if self.table is None:
      print("Table not found")
      return
    self.entry = self.table.getEntry(entryName)
    if self.entry is None:
      print("Entry not found")
      return
    self.entry.addListener(self.valueChanged, NetworkTables.NotifyFlags.UPDATE)

  def valueChanged(self, table, key, value, isNew):
    self.newValueAvailable.emit((key, value))

  def getValue(self):
    if self.table is None:
      return None
    return self.table.getValue(self.entryName, None)

  def putString(self, value):
    if self.entry is None:
      print("Entry not found")
      return 
    self.entry.setString(value)
