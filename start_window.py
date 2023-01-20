import sys
from GUI.UI.ui_start_window import Ui_Form as sw_ui
from GUI.UI.ui_create_train_menu import Ui_Form as tm_ui
from GUI.Widgets.training_main_window import TrainingMainWindow

from PySide6 import QtCore, QtWidgets, QtGui

class StartWindow(QtWidgets.QWidget, sw_ui):
    def __init__(self,) -> None:
        super().__init__()

        self.setupUi(self)
        self.ct_menu = CreateTrainMenu()
        self.training_window = TrainingMainWindow()

        # Connections
        self.train_button.clicked.connect(self.ct_menu.show)

        self.ct_menu.start_button.clicked.connect(self.close)
        self.ct_menu.start_button.clicked.connect(self.training_window.show)
        self.ct_menu.start_button.clicked.connect(self.ct_menu.close)



    
class CreateTrainMenu(QtWidgets.QWidget, tm_ui):
    def __init__(self,) -> None:
        super().__init__()

        self.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = StartWindow()

    widget.show()

    sys.exit(app.exec())