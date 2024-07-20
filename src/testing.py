import pickle
import train
from sklearn.metrics import accuracy_score

# Grab the best estimator from the training class
best_estimator = train.grid_search.best_estimator_

# Make predications based on the testing set
y_prediction = best_estimator.predict(train.x_test)

# Determine Accuracy Score
accuracy = accuracy_score(y_prediction, train.y_test)

# Print to review accuracy
print(f"{str(accuracy*100)}% of images were correctly classified.")

# Save model
pickle.dump(best_estimator, open('./model.p', 'wb'))

