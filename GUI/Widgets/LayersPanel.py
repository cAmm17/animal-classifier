"""
This file contains the layers panel for the image viewer project
"""

from PySide6 import QtCore, QtWidgets, QtGui

class LayersPanel(QtWidgets.QWidget):
    def __init__(self):
        # This is just a placeholder for visualizing the UI, it will not automatically create this many layers in the future
        self.layers = []

        menu = QtWidgets.QVBoxLayout()
        for i in range(4):
            layout = self._createLayer()
            self.layers.append(layout)
            menu.addLayout(layout)
        
        menu.setObjectName("layerMenu")
        self.layerMenu = menu


    def _createLayer(self):
        layer = QtWidgets.QHBoxLayout()
        layer.addWidget(QtWidgets.QCheckBox("Layer 0"))
        layer.addWidget(QtWidgets.QLabel("Test"))
        layer.setObjectName("layer")
        return layer
