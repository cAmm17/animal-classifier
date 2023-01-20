"""
This file provides the frontend GUI for the image window, which displays the current image (and will display layers once they are implememnted)

Interactions:
ImageEditAlgos - This file sends events and update information to this file. It then handles the update information based on the currently selected tool, using 
open cv and numpy. It then recieves the updated image from this file.
ImageLoader - Recieves the loaded in image from this class as well as sends the current image state when this image is saved or exported.

"""
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Signal, Slot
from ..algos.image_manager import ImageManager

class ImageWindow(QtWidgets.QWidget):
    #class members
    cur_image = []
    image_loaded = False

    def __init__(self):
        super().__init__()
        self.imageLabel = QtWidgets.QLabel(self)
        #set to a defualt test image for now
        pixmap = QtGui.QPixmap(1000, 800)
        pixmap.fill(QtGui.QColor("black"))

        self.resize(pixmap.width(), pixmap.height())
        #self.setGeometry(pixmap.width(), pixmap.height())
        self.imageLabel.setPixmap(pixmap)

    @Slot()
    def update_image(self):
        newImg = ImageManager.get_cur_image()
        w, h, chan = newImg.shape
        print(chan)
        currentQImage = QtGui.QImage(newImg.data, w, h, chan * w, QtGui.QImage.Format_RGB888)
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(currentQImage))

        
    
