from ..UI.ui_training import Ui_Form
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from ..algos.image_classifier import ImageClassifier

class Worker(QtCore.QObject):
    """This class is the worker thread used to run the image classifier"""
    finished = QtCore.Signal()
    progress = QtCore.Signal(int)

    def __init__(self, classifier, epochs) -> None:
        super().__init__()
        self.classifier = classifier
        self.epochs = epochs


    def run(self):
        # Run the training function for 1 epoch in a loop so that progress can be incrementally reported
        for i in range(self.epochs):
            self.classifier.train_model(1)
            self.progress.emit(i + 1)
        self.finished.emit()


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
            # run the classifier on a separate thread so that the GUI doesn't freeze up
            self.thread = QtCore.QThread()
            self.worker = Worker(self.image_classifier, int(num))

            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)

            self.thread.start()

    

