from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.title("Tkinter.com - Custom Tkinter!")
root.iconphoto("logom.png")
root.geometry("600x300")

my_button = customtkinter.CTkButton(root, text="Hello World!")
my_button.pack(pady = 80)


root.mainloop()