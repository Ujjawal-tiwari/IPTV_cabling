import tkinter as tk
from tkinter import filedialog
import vlc

# Load channels from the M3U playlist
def load_channels(file_path):
    channels = {}
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("#EXTINF:"):
                    parts = line.split(",")
                    channel_name = parts[1].strip()
                    channel_url = lines[lines.index(line) + 1].strip()
                    channels[channel_name] = channel_url
    except FileNotFoundError:
        print("File not found. Please select a valid M3U playlist.")
    return channels

# Play the selected channel
def play_channel():
    selected_channel = channel_listbox.get(tk.ACTIVE)
    if selected_channel in channel_urls:
        media = vlc.MediaPlayer(channel_urls[selected_channel])
        media.play()

# Load M3U playlist file
def load_playlist():
    file_path = filedialog.askopenfilename(filetypes=[("M3U Playlist", "*.m3u8")])
    if file_path:
        global channel_urls
        channel_urls = load_channels(file_path)
        channel_listbox.delete(0, tk.END)
        for channel in channel_urls:
            channel_listbox.insert(tk.END, channel)

# Create the main window
root = tk.Tk()
root.title("IPTV Player")
root.geometry("400x300")  # Set window size

# Styling
root.configure(bg="grey")

# Load playlist button
load_button = tk.Button(root, text="Load Playlist", command=load_playlist, bg="#4caf50", fg="white", font=("Arial", 22))
load_button.pack(pady=20)

# Channel listbox
channel_listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="black", fg="white", font=("Arial", 22))
channel_listbox.pack(expand=True, fill=tk.BOTH)

# Play button
play_button = tk.Button(root, text="Play Channel", command=play_channel, bg="#2196f3", fg="white", font=("Arial", 22))
play_button.pack(pady=20)

channel_urls = {}

# Start the GUI event loop
root.mainloop()
