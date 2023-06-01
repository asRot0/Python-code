import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Speech to Text')
window.geometry('500x200')

img = Image.open('icon.png')
img = img.resize((60,50), Image.LANCZOS)
icon_btn = ImageTk.PhotoImage(img)

microphone_button = tk.Button(window, image=icon_btn, borderwidth=0)
microphone_button.pack()

text_entry = tk.Text()


window.mainloop()