import tensorflow as tf
import numpy as np
from IPython.display import Image
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import cv2
from PIL import Image

file_path = 'G:/rauf/STEPBYSTEP/Data/dogcat/1.jpeg'

# display image first method with python
my_image_ipython = Image(file_path, width=224, height=224)
print(my_image_ipython)

# display image second method with keras
my_image_keras = image.load_img(file_path, target_size=(224, 224))
plt.imshow(my_image_keras)

# display image third method with cv2
my_image_cv2 = cv2.imread(file_path)
plt.imshow(my_image_cv2)

# display image fourth method with pillow
my_image_pillow = Image.open(file_path)
plt.imshow(my_image_pillow)

