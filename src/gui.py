from tkinter import *
import customtkinter as ctk
from PIL import Image
import classify
from skimage.io import imread


def nav_data():
    frame.pack_forget()
    data_frame.pack(pady=10, padx=15, fill="both", expand=True)
    data_frame.tkraise()
    label5.pack(pady=2, padx=10)
    print("Yes")


def nav_main():
    data_frame.pack_forget()
    frame.tkraise()
    frame.pack(pady=10, padx=15, fill="both", expand=True)


def test(image):
    prediction = classify.classify(image)
    if prediction == 0:
        type_label = "Benign"
    else:
        type_label = "Malignant"
    return type_label


def on_button_click1():
    type_label = test(ski_img)
    label2.configure(text="Tumor Type: " + type_label)


def on_button_click2():
    type_label = test(ski_img2)
    label3.configure(text="Tumor Type: " + type_label)


def on_button_click3():
    type_label = test(ski_img3)
    label4.configure(text="Tumor Type: " + type_label)


root = ctk.CTk()
root.geometry("600x800")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=10, padx=15, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Select an Image to Classify")
label.pack(pady=12, padx=10)

label2 = ctk.CTkLabel(master=frame, text="Tumor Type: ", font=("Arial", 14))
label2.pack(pady=2, padx=10)


img_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\malignant (1).png'
ski_img = imread('C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\malignant (1)_mask.png')
img = ctk.CTkImage(Image.open(img_path)
                             , size=(200, 150))
img_button = ctk.CTkButton(master=frame, text="", image=img, command=on_button_click1)
img_button.pack(pady=10)

# label2 = ctk.CTkLabel(master=frame, text="Select an Image to Classify", image=img)
# label2.pack(pady=12, padx=10)

label3 = ctk.CTkLabel(master=frame, text="Tumor Type: ", font=("Arial", 14))
label3.pack(pady=2, padx=10)

img2_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (1).png'
ski_img2 = imread('C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (1)_mask.png')
img2 = ctk.CTkImage(Image.open(img2_path)
                              , size=(200, 150))
img_button2 = ctk.CTkButton(master=frame,text="", image=img2, command=on_button_click2)
img_button2.pack(pady=10)

label4 = ctk.CTkLabel(master=frame, text="Tumor Type: ", font=("Arial", 14))
label4.pack(pady=2, padx=10)

img3_path = 'C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (2).png'
ski_img3 = imread('C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\GUIExamples\\benign (2)_mask.png')
img3 = ctk.CTkImage(Image.open(img3_path)
                              , size=(200, 150))
img_button3 = ctk.CTkButton(master=frame,text="", image=img3, command=on_button_click3)
img_button3.pack(pady=10)

nav_data_button = ctk.CTkButton(master=frame, text="Data Visualizations", command=nav_data)
nav_data_button.pack(side=BOTTOM, pady=20)

# DATA VISUALIZATION FRAME
data_frame = ctk.CTkFrame(master=root)
data_frame.pack(pady=10, padx=15, fill="both", expand=True)

label5 = ctk.CTkLabel(master=data_frame, text="Balls", font=("Arial", 14))

nav_main_button = ctk.CTkButton(master=data_frame, text="Home", command=nav_main)
nav_main_button.pack(side=BOTTOM, pady=20)

root.mainloop()
