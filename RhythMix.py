import os
import tkinter as tk
from tkinter import filedialog, ttk
from pygame import mixer
from mutagen.mp3 import MP3

mixer.init()

def play_music():
    selected_song = song_listbox.get(tk.ACTIVE)
    if selected_song:
        mixer.music.load(selected_song)
        mixer.music.play()
        update_song_details(selected_song)

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def add_songs():
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    for file in files:
        if file not in songs:
            songs.append(file)
            song_listbox.insert(tk.END, file)

def update_song_details(song_path):
    audio = MP3(song_path)
    song_length = audio.info.length
    mins, secs = divmod(int(song_length), 60)
    time_formatted = f"{mins}:{secs:02d}"
    song_details_label.config(text=f"Now Playing: {os.path.basename(song_path)} | Length: {time_formatted}")

songs = []

root = tk.Tk()
root.title("RhythMix")

# Create a canvas to be used as the main background
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack(fill=tk.BOTH, expand=True)

# Optional: add a background image to the canvas
# canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

main_frame = ttk.Frame(root, padding="10")
canvas.create_window(250, 250, window=main_frame)  # Place the frame inside the canvas

song_listbox = tk.Listbox(main_frame, height=15, width=50)
song_listbox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

play_button = ttk.Button(main_frame, text="Play", command=play_music)
play_button.grid(row=1, column=0, padx=5, pady=5)

stop_button = ttk.Button(main_frame, text="Stop", command=stop_music)
stop_button.grid(row=1, column=1, padx=5, pady=5)

pause_button = ttk.Button(main_frame, text="Pause", command=pause_music)
pause_button.grid(row=1, column=2, padx=5, pady=5)

resume_button = ttk.Button(main_frame, text="Resume", command=resume_music)
resume_button.grid(row=1, column=3, padx=5, pady=5)

add_button = ttk.Button(main_frame, text="Add Songs", command=add_songs)
add_button.grid(row=2, column=0, columnspan=4, pady=10)

song_details_label = ttk.Label(main_frame, text="Now Playing: None", anchor="center")
song_details_label.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()
