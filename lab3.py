import tkinter as tk
import random
import string


def key_gen():
    word = entry.get().upper()
    if len(word) != 6:
        key_label.config(text="only 6 letters!!!")
        return
    
    block1 = "".join(random.sample(word, 3))
    digits = [str((ord(c)-64)%10) for c in word]
    block2 = "".join(digits)[:6]
    block3 = "".join(random.sample(word, 3))
    key = f"{block1}-{block2}-{block3}"
    key_label.config(text=key)

root = tk.Tk()
root.title("keygen")
root.geometry("1230x700")

bg_photo = tk.PhotoImage(file="background.png")
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

entry = tk.Entry(root)
canvas.create_window(250, 380, window=entry)

button = tk.Button(root, text="generate key", command=key_gen)
canvas.create_window(250, 430, window=button)

key_label = tk.Label(root, text="Result:")
canvas.create_window(250, 480, window=key_label)

if __name__ == "__main__":
    root.mainloop()