from ..UI.ui_training import Ui_Form
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from ..algos.image_classifier import ImageClassifier

class TrainingMainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self,) -> None:
        super().__init__()

        self.setupUi(self)
        self.load_image_classifier()
        self.train_button.clicked.connect(self.train_classifier)

        # The currently open image classifier, to be passed from the start menu
        

    def load_image_classifier(self):
        self.image_classifier = ImageClassifier()
        # This is only hardcoded for now for testing, this will be passed from the start window later on
        self.image_classifier.setup_dataset("/home/ammcourt/repos/image_editor/data/images", .80)
        self.image_classifier.create_model(2)

    def train_classifier(self):
        #get epochs from text window
        num = self.training_epochs_number.toPlainText()

        # add else with error popup here later to indicate the number is out of range/not a number
        if num.isdigit() and int(num) > 0 and int(num) < 100:
            #need to thread off and read in stdout using q text stream
            # readIn = QtCore.QTextStream(sys.stdout)
            self.image_classifier.train_model(int(num))

    

