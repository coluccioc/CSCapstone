import os
from skimage.io import imread
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import preprocess
import pickle
import train
from sklearn.metrics import accuracy_score

best_estimator = train.grid_search.best_estimator_

y_prediction = best_estimator.predict(train.x_test)

accuracy = accuracy_score(y_prediction, train.y_test)

print(f"{str(accuracy*100)}% of images were correctly classified.")

pickle.dump(best_estimator, open('./model.p', 'wb'))

