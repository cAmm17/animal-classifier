"""
This is the top level main window for the Image Editor program. It is built from widgets defined in the widegets folder
"""
import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Signal, Slot, Qt
from PySide6.QtWidgets import QToolBar, QLabel, QVBoxLayout, QHBoxLayout, QCheckBox, QMainWindow, QMenu
from PySide6.QtGui import QPixmap

from GUI.Widgets.MenuBar import MenuBar
from GUI.Widgets.ToolShelf import ToolShelf
from GUI.Widgets.ImageWindow import ImageWindow
from GUI.Widgets.LayersPanel import LayersPanel

class ImageEditor(QMainWindow):
      def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 500, 300)

        #initiate widgets
        menuBar = MenuBar(self)
        self.setMenuBar(menuBar)

        tools = ToolShelf()
        self.addToolBar(tools.toolBar)

        imageWindow = ImageWindow()

        layersPanel = LayersPanel()

        #connections
        menuBar.fileManager.loadImage.connect(imageWindow.updateImage)


        #add widgets and layouts to central widget
        centralWidget = QtWidgets.QWidget()
        layout = QHBoxLayout()
        layout.addWidget(imageWindow, 4)
        layout.addLayout(layersPanel.layerMenu, 1)
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ImageEditor()
    widget.resize(800, 600)

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    widget.show()

    sys.exit(app.exec())