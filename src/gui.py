from tkinter import *
import customtkinter
from PIL import Image


def test():
    print('Pog')


root = customtkinter.CTk()
root.geometry("600x1200")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=15, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Select an Image to Classify")
label.pack(pady=12, padx=10)

img = customtkinter.CTkImage(Image.open('C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\tumor.jpg')
                             , size=(200, 150))
img_button = customtkinter.CTkButton(master=frame, text="Malignant", image=img, command=test, width=500, height=200)
img_button.pack(pady=10)

label2 = customtkinter.CTkLabel(master=frame, text="Select an Image to Classify", image=img)
label2.pack(pady=12, padx=10)

img2 = customtkinter.CTkImage(Image.open('C:\\Users\\clcol\\PycharmProjects\\csCapstone\\images\\tumor2.png')
                              , size=(200, 150))
img_button2 = customtkinter.CTkButton(master=frame, text="Benign", image=img2, command=test, width=500, height=200)
img_button2.pack(pady=10)

root.mainloop()

