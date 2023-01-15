
from tensorflow import keras
import csv
import requests

def download_images_from_url(dataset_path, download_location):
    #for now, this function must be given a precreated folder to save the data to
    #this may  be changed in the future
    with open(dataset_path) as f:
        reader = csv.reader(f)
        
        img_url = -1
        species = -1
        filenum = 0

        for row in reader:
            # find the image url column
            if img_url < 0:
                for col in row:
                    img_url += 1
                    if col == 'image_url':
                        break
            else:
                download_image(row[img_url], download_location, str(filenum))
                filenum += 1


def download_image(image_url, download_location, filename):
    img_data = requests.get(image_url).content
    with open("/".join(download_location, filename), 'wb') as f:
        f.write(img_data)



