import tkinter as tk
from tkinter import ttk  # Import ttk explicitly

import pyttsx3

def text_to_speech():
    text = text_entry.get("1.0", "end-1c")
    rate = int(speed_entry.get())
    voice_id = voice_dropdown.current()
    
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.say(text)
    engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Text to Speech")

# Text Entry
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# Speed Entry
speed_label = tk.Label(root, text="Speed:")
speed_label.pack()
speed_entry = tk.Entry(root)
speed_entry.insert(0, "150")
speed_entry.pack()

# Voice Selection
voice_label = tk.Label(root, text="Voice:")
voice_label.pack()
voices = pyttsx3.init().getProperty('voices')
voice_options = [voice.name for voice in voices]
voice_dropdown = ttk.Combobox(root, values=voice_options, state="readonly")  # Use ttk here
voice_dropdown.current(0)
voice_dropdown.pack()

# Button to start text-to-speech
speech_button = tk.Button(root, text="Convert to Speech", command=text_to_speech)
speech_button.pack(pady=10)

root.mainloop()
