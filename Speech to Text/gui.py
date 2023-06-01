import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Speech to Text')
window.geometry('500x200')

img = Image.open('icon.png')
img = img.resize((60,50), Image.LANCZOS)
icon_btn = ImageTk.PhotoImage(img)

microphone_button = tk.Button(window, image=icon_btn, borderwidth=0)
microphone_button.grid(row=0, column=0)

side_text = tk.Text(window, height=5, width=15)
side_text.grid(row=1, column=0, rowspan=2)

text_entry = tk.Text(window, height=10, width=40)
text_entry.grid(row=0, column=1, rowspan=2, padx=45, pady=2)


window.mainloop()