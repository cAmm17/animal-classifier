from ..UI.ui_training import Ui_Form

from PySide6 import QtCore, QtWidgets, QtGui

class TrainingMainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self,) -> None:
        super().__init__()

        self.setupUi(self)

        #connect training button to open up menu
        

