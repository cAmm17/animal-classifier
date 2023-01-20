"""
This file contains the code for the image classifier. 
"""

import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential

class ImageClassifier:
    def __init__(self) -> None:
        self.model_loaded = False
        self.train_ds = None
        self.val_ds = None
        pass

    def setup_dataset(self, directory, val_split, data_seed = 100) -> None:
        #probably pass these in
        batch_size = 32
        img_height = 180
        img_width = 180
        #should change this to not be based on directories once the model is working
        self.train_ds = keras.utils.image_dataset_from_directory(
        directory, 
        validation_split = val_split,
        subset="training",
        seed=data_seed,
        image_size=(img_height, img_width),
        batch_size=batch_size)

        self.val_ds = keras.utils.image_dataset_from_directory(
            directory, 
            validation_split = val_split,
            subset="validation",
            seed=data_seed,
            image_size=(img_height, img_width),
            batch_size=batch_size)
        return
    
    def create_model(self, num_classes):
        batch_size = 32
        img_height = 180
        img_width = 180

        self.model = Sequential([
        layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
        ])

        self.model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

        print(self.model.summary())
        self.model_loaded = True
        return

    def load_model(self, path):
        self.model = keras.models.load_model(path)


    def save_model(self, path):
        self.model.save(path)
    
    def train_model(self, epochs = 10):
        if self.model_loaded:
            history = self.model.fit(
                self.train_ds,
                validation_data=self.val_ds,
                epochs=epochs)
                


if __name__ == "__main__":
    m = ImageClassifier()
    m.setup_dataset("../../data/images/", .80)
    m.create_model(2)
    m.train_model()