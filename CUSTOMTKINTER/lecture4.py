# TabView

import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x300")

tabView = customtkinter.CTkTabview(app)
tabView.pack(padx = 20, pady = 20)

tabView.add("tab-1")
tabView.add("tab-2")
tabView.add("tab-3")

tabView.set("tab-1") # it opens as default

def button_function1():
    print("Button 1 pressed")
def button_function2():
    print("Button 2 pressed")
def button_function3():
    print("Button 3 pressed")

button_1 = customtkinter.CTkButton(tabView.tab("tab-1"), text = "Button 1", command=button_function1)
button_1.pack(padx = 20, pady = 20)

button_2 = customtkinter.CTkButton(tabView.tab("tab-2"), text = "Button 2", command=button_function2)
button_2.pack(padx = 20, pady = 20)

button_3 = customtkinter.CTkButton(tabView.tab("tab-3"), text = "Button 3",command=button_function3)
button_3.pack(padx = 20, pady = 20)

app.mainloop()