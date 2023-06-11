import tkinter as tk
from tkVideoPlayer import TkinterVideo
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# set to fullscreen
app.attributes("-fullscreen", True)


def button_function():
    file = tk.filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))

    # Create a video player

    videoplayer = TkinterVideo(master=app, scaled=True)
    videoplayer.load(file)
    videoplayer.pack(expand=True, fill="both")

    videoplayer.play()  # play the video


# Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(
#     master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# Make a button to select a file
button = tk.Button(master=app, text="Select file", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


app.mainloop()
