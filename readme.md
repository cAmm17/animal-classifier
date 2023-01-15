## Description

This is a simple utility app used for training animal image classifiers. It has a GUI that allows users to both train and run results through the model, as well as utilities to help with model training and processing image datasets with a specific focus on iNaturalist data. This was inspired by a need to automatically classify animals from image and sensor data.

Note: I was originally going to make this application an image editor, so there may still be some files referring to that. These references will be removed as development continues.


## Specifications
The following libraries are used by this application:

    * PySide6 (QT for python) - For the app's GUI
    * Tensorflow 2 and Keras - Used to build the image classification model
    * OpenCV


## Installation


## Currently in progress
* Getting the basic model set up and setting up the GUI for training the model

## Full project plans

### Basic Planned Functionality:
* An Image classifier built in Tensorflow and Keras with some pre-trained data on common species.
* Ability to run the model on a given dataset and output the results to a file or folder
* Utilities for looking at output data, including:
    * Lists of least confident guesses and most confident guesses of images, which can be viewed in the app. Images can also be removed via these lists or added to a run or training dataset.
    * Graphs of confidence rating data to see how the model is doing on that dataset
* Ability to provide train the model in the app.
* Utilities to train the model, including:
    * Display for graphs to view how model training is going over time
    * Ability to add additional data augmentation to generate additional training data and help with model overfitting.
* Utilities for data processing, including:
    * Ability to take csv datasets with (optionally) species names and image urls and retrieve and organize the images from that dataset
    * Integration with the iNaturalist api to get additional data from the app


### Possible Future Functionality:
* Object Identification (likely using OpenCV), which would also allow for additional data like number of found animals across the dataset where there may be multiple animals in the same image
* Possible extensions for other model types (likely still focusing on ecological data) or other image types using object recognition (like satellite data)