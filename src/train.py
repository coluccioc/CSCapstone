import os
from skimage.io import imread
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import preprocess


# Split Data into Train / Test
x_train, x_test, y_train, y_test = train_test_split(preprocess.data, preprocess.labels, test_size=0.2,
                                                    shuffle=True, stratify=preprocess.labels)
# Train the classifier
classifier = SVC()

parameters = [{'gamma': [.01, .001, .0001], 'C': [1, 10, 100, 1000]}]

grid_search = GridSearchCV(classifier, parameters)

grid_search.fit(x_train, y_train)
