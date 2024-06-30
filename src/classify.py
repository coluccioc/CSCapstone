import pickle
import preprocess

model_path = './model.p'

with open(model_path, 'rb') as model_file:
    classifier = pickle.load(model_file)


def classify(image):
    image = preprocess.preprocess(image)
    image = image.reshape(1, -1)
    return classifier.predict(image)
