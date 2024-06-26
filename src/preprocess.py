import os
from skimage.io import imread
from skimage.transform import resize
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

input_dir = r'C:\Users\clcol\PycharmProjects\csCapstone\images\benign'
categories = ['benign', 'malignant']

data = []
labels = []

for index, category in enumerate(categories):
    for file in os.listdir(input_dir):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        resize(img, (250, 250))
        data.append(img.flatten())
        labels.append(index)

data = np.asarray(data)
labels = np.asarray(labels)