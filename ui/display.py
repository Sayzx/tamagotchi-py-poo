import tkinter as tk
from tkinter import scrolledtext
import os
import itertools

def get_ascii_art(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return ["ASCII art non trouvé.\n"]

def animate_ascii(text_widget, frames, delay=200, index=0):
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.INSERT, "".join(frames[index]))
    index = (index + 1) % len(frames)
    text_widget.after(delay, animate_ascii, text_widget, frames, delay, index)

def show_creature_ascii(creature):
    filename = os.path.join(os.path.dirname(__file__), "art", f"{creature.type.lower()}.txt")
    
    if not os.path.exists(filename):  # Vérifie si le fichier existe
        print(f"⚠️ Fichier non trouvé : {filename}")
        return

    frames = [get_ascii_art(filename)]

    window = tk.Tk()
    window.title(f"{creature.name} ({creature.type})")
    window.geometry("800x600")  

    text_widget = scrolledtext.ScrolledText(window, width=100, height=30)
    text_widget.pack()

    animate_ascii(text_widget, frames)

    window.mainloop()
