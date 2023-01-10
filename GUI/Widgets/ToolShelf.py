"""
This file contains the UI for the tool shelf, which is composed of the ToolButtons of the currently available tools

Interactions:
ToolButton - Used as widgets to display each tool

"""
from PySide6 import QtCore, QtWidgets, QtGui

class ToolShelf(QtWidgets.QWidget):
      def __init__(self):
         self.toolBar = QtWidgets.QToolBar("Edit")
      
