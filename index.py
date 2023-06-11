import tkinter as tk
from tkVideoPlayer import TkinterVideo
import customtkinter as ctk
from moviepy.editor import VideoFileClip
import vlc


def button_function():
    file = tk.filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("mp4 files", "*.mp4"), ("all files", "*.*")))

    instance = vlc.Instance()
    media = instance.media_new(file)
    player = instance.media_player_new()
    player.set_media(media)
    player.set_hwnd(ctkFrame.winfo_id())
    player.play()

    video_clip = VideoFileClip(file)
    audio_clip = video_clip.audio


if __name__ == "__main__":
    # Modes: system (default), light, dark
    ctk.set_appearance_mode("System")
    # Themes: blue (default), dark-blue, green
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("IntelliSub")
    root.after(0, lambda: root.wm_state('zoomed'))

    ctkFrame = ctk.CTkFrame(root)

    button = ctk.CTkButton(
        master=ctkFrame, text="Select file", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    ctkFrame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
