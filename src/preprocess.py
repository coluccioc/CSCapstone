import os
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgba2rgb, rgb2gray
import numpy as np

# DELETING FILES THAT ARE NOT MASKED
# folder_path = r'C:\Users\clcol\PycharmProjects\csCapstone\images\benign'
#
# for filename in os.listdir(folder_path):
#     if "mask" not in filename:
#         file_path = os.path.join(folder_path, filename)
#
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#             print(f"deleted: {file_path}")
# print('done')

input_dir = r'C:\Users\clcol\PycharmProjects\csCapstone\images'
categories = ['benign', 'malignant']

data = []
labels = []


def preprocess(image):
    # shape showing 4 as the last value indicates an rgba. must convert to rbg
    # shape showing 3 as the last value indicates a color rgb. must convert to gray
    if image.shape[-1] == 4:
        image = rgba2rgb(image)
    if image.shape[-1] == 3:
        image = rgb2gray(image)

    resized_image = resize(image, (250, 250), anti_aliasing=False)
    flattened_image = resized_image.flatten()

    return flattened_image


for index, category in enumerate(categories):
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)

        data.append(preprocess(img))
        labels.append(index)

data = np.asarray(data)
labels = np.asarray(labels)
