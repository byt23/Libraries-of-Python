# Label

# Scrollbar

import customtkinter, tkinter
from tkinter import *

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x300")

frame = customtkinter.CTkFrame(master = app, width = 200, height=200, corner_radius=10)
frame.pack(padx = 20, pady = 20)

tk_textbox = tkinter.Text(frame, highlightthickness=0)
tk_textbox.grid(row=0, column = 0, sticky="nsew")

my_string_var = StringVar()

ctk_textbox_scrollbar = customtkinter.CTkScrollbar(frame, command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row = 0, column= 1, sticky = "ns")

tk_textbox.configure(yscrollcommand= ctk_textbox_scrollbar.set)

def button_event():
    textbox_text = tk_textbox.get("0.0","end")
    my_string_var.set(str(textbox_text))

button = customtkinter.CTkButton(master=frame, text = "Button", command=button_event) 
button.grid(padx = 20, pady = 10)

label = customtkinter.CTkLabel(master=frame, textvariable = my_string_var, width=120, height=25, fg_color=("white","black"),corner_radius=8)
label.grid(padx = 20, pady = 10)

app.mainloop()