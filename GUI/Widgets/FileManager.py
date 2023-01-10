from PySide6 import QtCore, QtWidgets, QtGui
from ..algos.ImageManager import ImageManager

class FileManager(QtWidgets.QMenu):
    loadImage = QtCore.Signal()

    def __init__(self, parent = None):
        QtWidgets.QMenu.__init__(self, parent)
        #self.fileMenu = QtWidgets.QMenu("&File")
        self.setTitle("&File")

        save_action = QtGui.QAction("&Save", self)
        save_action.setToolTip("Save the current file")
        save_action.triggered.connect(self.saveFile)
        self.addAction(save_action)
        #add save as here later

        load_action = QtGui.QAction("&Load", self)
        load_action.setToolTip("Load in a new file")
        load_action.triggered.connect(self.loadFile)
        self.addAction(load_action)

    def loadFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "./", "Image Files (*.png *.jpg *.bmp)")
        #check if file is valid then pass to image loader
        if filename != "" and filename is not None:
            print(type(filename))
            print(type(filename[0]))
            success, msg = ImageManager.load_file(filename[0])
            if success:
                self.loadImage.emit()
            else:
                print(msg)
        #if manager returns success, signal new file opened to get the pixmap to check the backend image for an update

    def saveFile(self):
        # add differentiation for exisiting files here later
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save File",
                                       "./untitled.png",
                                        "Images (*.png *.xpm *.jpg)")
        #call file manager  to save
        if filename != "" and filename is not None:
            print(filename)
            success, msg = ImageManager.save_file(filename[0])
            if not success:
                print(msg)
                
            #sucess, msg = imageLoader.save(filename)