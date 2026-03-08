import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x300")

frame = customtkinter.CTkFrame(master = app,
                               width = 200,
                               height = 200,
                               corner_radius = 30,
                               bg_color = "yellow")


frame.pack(padx = 30, pady = 30)

def button_function1() :
    print("button1 pressed!")

def button_function2(): 
    print("button2 pressed!")

button1 = customtkinter.CTkButton(master = frame, text = "Button_1", command = button_function1)
button1.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

button2 = customtkinter.CTkButton(master = frame, text = "Button_2", command = button_function2)
button2.place(relx = 0.5, rely = 0.8, anchor = tkinter.CENTER)

app.mainloop()