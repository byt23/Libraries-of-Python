# Text Box

import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x300")

textbox = customtkinter.CTkTextbox(app)
textbox.grid(row = 0, column = 0)

text = """
Welcome to BYT Software
"""
textbox.insert("0.0", text)
textbox.configure(state = "normal")

def button_clicked():
    print(textbox.get("0.0","end"))

button = customtkinter.CTkButton(master = app, text="CTkButton", command = button_clicked)
button.place(relx = 0.7, rely = 0.3, anchor = tkinter.CENTER)

app.mainloop()
