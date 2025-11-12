import tkinter as tk
import random
import string

WINDOW_TITLE = "keygen"
WINDOW_SIZE = "1230x700"
BACKGROUND_IMAGE = "background.png"
ENTRY_POSITION = (250, 380)
BUTTON_POSITION = (250, 430)
LABEL_POSITION = (250, 480)
REQUIRED_WORD_LENGTH = 6
BLOCK_LENGTH = 3
DIGIT_OFFSET = 64


def key_gen():
    word = entry.get().upper()
    if len(word) != REQUIRED_WORD_LENGTH:
        key_label.config(text="only 6 letters!!!")
        return
    
    block1 = "".join(random.sample(word, BLOCK_LENGTH))
    digits = [str((ord(c) - DIGIT_OFFSET) % 10) for c in word]
    block2 = "".join(digits)[:REQUIRED_WORD_LENGTH]
    block3 = "".join(random.sample(word, BLOCK_LENGTH))
    key = f"{block1}-{block2}-{block3}"
    key_label.config(text=key)


root = tk.Tk()
root.title(WINDOW_TITLE)
root.geometry(WINDOW_SIZE)

bg_photo = tk.PhotoImage(file=BACKGROUND_IMAGE)
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

entry = tk.Entry(root)
canvas.create_window(ENTRY_POSITION[0], ENTRY_POSITION[1], window=entry)

button = tk.Button(root, text="generate key", command=key_gen)
canvas.create_window(BUTTON_POSITION[0], BUTTON_POSITION[1], window=button)

key_label = tk.Label(root, text="Result:")
canvas.create_window(LABEL_POSITION[0], LABEL_POSITION[1], window=key_label)

if __name__ == "__main__":
    root.mainloop()