import tkinter as tk
import pyttsx3

def convert_to_speech():
    text = text_input.get()
    if text:
        engine.setProperty('rate', 190)
        engine.setProperty('volume', 0.8)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

        engine.say(text)
        engine.runAndWait()

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Create the Tkinter window
window = tk.Tk()
window.title("Text to Speech")
window.geometry('500x150')
window.configure(bg='#DDE9E4')
window.resizable(False, False)

# Create a label and text input field
label = tk.Label(window, text="Enter text:", bg='#DDE9E4')
label.grid(row=0, column=0, pady=2)

text_input = tk.Entry(window, width=40, bg='#E0E1E2')
text_input.grid(row=0, column=1)

# Create a button to convert text to speech
convert_button = tk.Button(window, text="Convert to Speech",bg='#A29FA5', command=convert_to_speech)
convert_button.grid(row=1, column=1, sticky='e', pady=2)

# Start the Tkinter event loop
window.mainloop()
