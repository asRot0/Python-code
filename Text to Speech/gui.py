import tkinter as tk
import pyttsx3

def convert_to_speech():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Create the Tkinter window
window = tk.Tk()
window.title("Text-to-Speech")

# Create a text input field
text_input = tk.Text(window, height=10, width=50)
text_input.pack()

# Create a button to convert text to speech
convert_button = tk.Button(window, text="Convert to Speech", command=convert_to_speech)
convert_button.pack()

# Start the Tkinter event loop
window.mainloop()
