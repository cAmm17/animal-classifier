""" 
This class contains the algorithms used for image saving and loading. It provides the backend algorithms for image window and menus, which contain the frontend ui
"""
import cv2 as cv

class ImageManager:
    currentImage = None
    # may include support for multiple open images here later

    @classmethod
    def save_file(cls, fileName):
        success = False
        msg = 'No Image Available'

        success = cv.imwrite(fileName, cls.currentImage)
        
        if not success:
            msg = "Error: Failed to write image"

        return success, msg

    @classmethod
    def load_file(cls, fileName):
        """Loads an image from a selected file and returns if the image was loaded successfully, plus and error message if it was not"""
        success = False
        msg = 'No Image Available'

        img = cv.imread(fileName, cv.IMREAD_COLOR)

        if img is None:
            success = False
            msg = "Error: Failed to read image"
        else:
            cls.currentImage = img
            success = True

        return success, msg

    @classmethod
    def get_cur_image(cls):
        return cv.cvtColor(cls.currentImage,  cv.COLOR_BGR2RGB)