import tkinter as tk
import speech_recognition as sr

def convert_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text_entry.delete(1.0, tk.END)
        text_entry.insert(tk.END, text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError:
        print("Sorry, could not connect to the speech recognition service.")

# Create the Tkinter window
window = tk.Tk()
window.title("Speech to Text")

# Create a button to initiate speech-to-text conversion
convert_button = tk.Button(window, text="Convert", command=convert_speech)
convert_button.pack()

# Create a text entry field to display the converted text
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Start the Tkinter event loop
window.mainloop()
