import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

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
    img = img.resize((100,100))
    ax.imshow(img)
    ax.axis('off')

for ax in axes[len(img_paths):]:
    ax.axis('off')

axes[0].set_title('Benign')
axes[1].set_title('Malignant')


plt.tight_layout()
plt.savefig('img_grid')
plt.show()


