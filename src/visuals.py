import matplotlib.pyplot as plt
from PIL import Image
from sklearn.metrics import confusion_matrix
import seaborn as sns
import train
import testing

labels = 'Benign', 'Malignant'
sizes = [437, 210]  # Replace with your actual counts
colors = ['Green', 'Red']
explode = (0.1, 0)  # explode 1st slice

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.set_title('Percentage of Benign vs Malignant Tumors')

plt.savefig('pie_chart.png')
plt.close(fig)

img_paths = ['C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (1).png',
             'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\malignant (1).png',
             'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (2).png',
             'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\malignant (2).png',
             'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (3).png',
             'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\malignant (3).png']

fig, axes = plt.subplots(3, 2, figsize=(8, 8))
axes = axes.flatten()

for ax, img_path in zip(axes, img_paths):
    img = Image.open(img_path)
    img = img.resize((100, 100))
    ax.imshow(img)
    ax.axis('off')

for ax in axes[len(img_paths):]:
    ax.axis('off')

axes[0].set_title('Benign')
axes[1].set_title('Malignant')


plt.tight_layout()
plt.savefig('img_grid')
plt.close(fig)

cm = confusion_matrix(train.y_test, testing.y_prediction)

class_names = ['Benign', 'Malignant']


def create_confusion_matrix(confmatrix, classes, cm_image_path):
    figure, axis = plt.subplots(figsize=(8, 8))
    sns.heatmap(confmatrix, annot=True, fmt='d', cmap='Blues', ax=axis,
                xticklabels=classes, yticklabels=classes)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion Matrix')
    figure.savefig(cm_image_path)
    plt.close(figure)


create_confusion_matrix(cm, class_names, 'confusion_matrix.png')
