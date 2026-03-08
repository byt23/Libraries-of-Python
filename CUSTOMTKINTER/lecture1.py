import customtkinter

# THEME
customtkinter.set_appearance_mode("system") # system - dark - light
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("Customtkinter App By BYT") # TITLE
app.geometry("500x500") # SIZE

app.mainloop()

