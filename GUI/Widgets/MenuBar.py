from PySide6 import QtCore, QtWidgets, QtGui
from .FileManager import FileManager

class MenuBar(QtWidgets.QMenuBar):
  fileManager = None

  def __init__(self, parent = None):
    QtWidgets.QMenuBar.__init__(self, parent)

    #probably will move this to be instantiated somewhere else in the future since file manager functionality may be used in other areas of the app
    self.fileManager = FileManager()

    fileMenu = self.addMenu(self.fileManager)
    editMenu = self.addMenu("&Edit")
    helpMenu = self.addMenu("&Help")
