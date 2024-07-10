from tkinter import *
import customtkinter as ctk
from PIL import Image
import classify
from skimage.io import imread
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Navigate to the First Data Visualization Scene
def nav_data():
    frame.pack_forget()
    data_frame.pack(pady=10, padx=15, fill="both", expand=True)
    data_frame.tkraise()
    label5.pack(pady=2, padx=10)
    pie_label.pack(pady=12, padx=10)
    grid_label.pack(pady=12, padx=10)
    nav_main_button.pack(side=BOTTOM, pady=20)
    nav_data2_button.pack(side=BOTTOM, pady=10)


# Navigate to the Second Data Visualization Scene
def nav_data2():
    data_frame.pack_forget()
    data_frame2.pack(pady=10, padx=15, fill="both", expand=True)
    data_frame2.tkraise()
    nav_main_button2.pack(side=BOTTOM, pady=20)
    nav_data3_button.pack(side=BOTTOM, pady=10)


# Navigate to the Third Data Visualization Scene
def nav_data3():
    data_frame2.pack_forget()
    data_frame3.pack(pady=10, padx=15, fill="both", expand=True)
    data_frame3.tkraise()
    nav_main_button3.pack(side=BOTTOM, pady=20)


# Navigate to the Home Scene (from the data1 scene)
def nav_main():
    data_frame.pack_forget()
    frame.tkraise()
    frame.pack(pady=10, padx=15, fill="both", expand=True)


# Navigate to the Home Scene (from data2 scene)
def nav_main2():
    data_frame2.pack_forget()
    frame.tkraise()
    frame.pack(pady=10, padx=15, fill="both", expand=True)


# Navigate to the Home Scene (from data3 scene)
def nav_main3():
    data_frame3.pack_forget()
    frame.tkraise()
    frame.pack(pady=10, padx=15, fill="both", expand=True)


# Argument is image. Image is passed to be classified as Benign or Malignant
def test(image):
    prediction = classify.classify(image)
    if prediction == 0:
        type_label = "Benign"
    else:
        type_label = "Malignant"
    return type_label


# 1st image clicked, populate classification
def on_button_click1():
    type_label = test(ski_img)
    label2.configure(text="Tumor Type: " + type_label)


# 2nd image clicked, populate classification
def on_button_click2():
    type_label = test(ski_img2)
    label3.configure(text="Tumor Type: " + type_label)


# 3rd image clicked, populate classification
def on_button_click3():
    type_label = test(ski_img3)
    label4.configure(text="Tumor Type: " + type_label)


# Establish root & initial home frame
root = ctk.CTk()
root.geometry("600x800")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=10, padx=15, fill="both", expand=True)

# Create labels & images. 3 Examples that can be clicked to classify using the ML model
label = ctk.CTkLabel(master=frame, text="Select an Image to Classify")
label.pack(pady=12, padx=10)

label2 = ctk.CTkLabel(master=frame, text="Tumor Type: ", font=("Arial", 14))
label2.pack(pady=2, padx=10)

img_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\malignant (1).png'
ski_img = imread('C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\malignant (1)_mask.png')
img = ctk.CTkImage(Image.open(img_path), size=(200, 150))
img_button = ctk.CTkButton(master=frame, text="", image=img, command=on_button_click1)
img_button.pack(pady=10)

# label2 = ctk.CTkLabel(master=frame, text="Select an Image to Classify", image=img)
# label2.pack(pady=12, padx=10)

label3 = ctk.CTkLabel(master=frame, text="Tumor Type: ", font=("Arial", 14))
label3.pack(pady=2, padx=10)

img2_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (1).png'
ski_img2 = imread('C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (1)_mask.png')
img2 = ctk.CTkImage(Image.open(img2_path), size=(200, 150))
img_button2 = ctk.CTkButton(master=frame, text="", image=img2, command=on_button_click2)
img_button2.pack(pady=10)

label4 = ctk.CTkLabel(master=frame, text="Tumor Type: ", font=("Arial", 14))
label4.pack(pady=2, padx=10)

img3_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (2).png'
ski_img3 = imread('C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (2)_mask.png')
img3 = ctk.CTkImage(Image.open(img3_path), size=(200, 150))
img_button3 = ctk.CTkButton(master=frame,text="", image=img3, command=on_button_click3)
img_button3.pack(pady=10)

nav_data_button = ctk.CTkButton(master=frame, text="Data Visualizations", command=nav_data)
nav_data_button.pack(side=BOTTOM, pady=20)

# DATA VISUALIZATION FRAME 1
data_frame = ctk.CTkFrame(master=root)

label5 = ctk.CTkLabel(master=data_frame, text="Visualizations", font=("Arial", 14))

img4_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\src\\pie_chart.png'
img4 = ctk.CTkImage(Image.open(img4_path), size=(500, 400))
pie_label = ctk.CTkLabel(master=data_frame, text="", image=img4)

nav_data2_button = ctk.CTkButton(master=data_frame, text="NEXT", command=nav_data2)
nav_main_button = ctk.CTkButton(master=data_frame, text="Home", command=nav_main)

# DATA VISUALIZATION FRAME 2
data_frame2 = ctk.CTkFrame(master=root)

label7 = ctk.CTkLabel(master=data_frame2, text="Visualizations", font=("Arial", 14))

img5_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\src\\img_grid.png'
img5 = ctk.CTkImage(Image.open(img5_path), size=(500, 400))
grid_label = ctk.CTkLabel(master=data_frame2, text="", image=img5)

nav_data3_button = ctk.CTkButton(master=data_frame2, text="NEXT", command=nav_data3)
nav_main_button2 = ctk.CTkButton(master=data_frame2, text="Home", command=nav_main2)

# DATA VISUALIZATION FRAME 3
data_frame3 = ctk.CTkFrame(master=root)

label8 = ctk.CTkLabel(master=data_frame2, text="Visualizations", font=("Arial", 14))

img6_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\src\\img_grid.png'
img6 = ctk.CTkImage(Image.open(img6_path), size=(200, 200))
matrix_label = ctk.CTkLabel(master=data_frame3, text="", image=img6)

nav_main_button3 = ctk.CTkButton(master=data_frame3, text="Home", command=nav_main3)

root.mainloop()
