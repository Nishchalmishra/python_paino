import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import os

# play 
def play_note(note):
    folder = 'notes'
    filename = os.path.join(folder, f"{note}.wav")
    if os.path.exists(filename):
        playsound(filename)
    else:
        messagebox.showerror("ERROR: File note found")

root = tk.Tk()
root.title("Paino")

white_keys = ['C','D','E','F','G','A','B','C1','D1','E2','F1']
black_keys = ['Cs','Ds','D','Fs','Gs','Bb', 'D', 'Cs1', 'Ds1']

white_key_width = 150
white_key_height = 500
black_key_width = 150
black_key_height = 300

for i,key in enumerate(white_keys):
    btn = tk.Button(root, text=key, bg='white',fg='black',
                    height=white_key_height // 20, width=white_key_width // 10,
                    command=lambda note = key: play_note(note))
    btn.place(x=i * white_key_width, y=0)


for i,key in enumerate(black_keys):
    btn = tk.Button(root, text=key, bg='black',fg='white',
                    height=black_key_height // 20, width=black_key_width // 10,
                    command=lambda note = key: play_note(note))
    btn.place(x=(i * black_key_width) + (white_key_width - black_key_width // 2), y=0)


root.geometry(f"{len(white_keys) * white_key_width}x{white_key_height}")

root.mainloop()


    