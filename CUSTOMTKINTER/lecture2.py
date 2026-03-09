# Button


import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("Customtkinter App By BYT")
app.geometry("300x300")

def button_function():
    print("Button Pressed !")

button = customtkinter.CTkButton(master = app, text = "BYT Software", command=button_function)
button.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

app.mainloop()