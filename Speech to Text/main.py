import tkinter as tk
import speech_recognition as sr
from PIL import Image, ImageTk
import pyttsx3
from threading import Thread


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()

    side_text.delete(1.0, tk.END)
    side_text.insert(tk.END, command)

    engine.say(command)
    engine.runAndWait()


def start_listening():
    global count
    count += 1
    side_text.delete(1.0, tk.END)
    message = 'listening...'
    side_text.insert(tk.END, message + str(count))

    # By using a separate thread for the speech-to-text
    # conversion, the GUI remains responsive while the conversion process is taking place.
    Thread(target=convert_speech).start()


def convert_speech():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        recognizer.adjust_for_ambient_noise(source, duration=0.1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()

        text_entry.delete(1.0, tk.END)
        text_entry.insert(tk.END, text)

    except sr.UnknownValueError:
        SpeakText('Sorry, I could not understand audio.')

    except sr.RequestError as e:
        SpeakText('Could not request results; {0}'.format(e))


# Create the Tkinter window
window = tk.Tk()
window.title('Speech to Text')
window.geometry('500x200')
window.resizable(False, False)
count = 0

img = Image.open('icon.png')
img = img.resize((60,50), Image.LANCZOS)
icon_btn = ImageTk.PhotoImage(img)


# Create a button to initiate speech-to-text conversion
microphone_button = tk.Button(window, image=icon_btn, borderwidth=0, command=start_listening)
microphone_button.grid(row=0, column=0)

side_text = tk.Text(window, height=5, width=15)
side_text.grid(row=1, column=0, rowspan=2)

# Create a text entry field to display the converted text
text_entry = tk.Text(window, height=10, width=40)
text_entry.grid(row=0, column=1, rowspan=2, padx=45, pady=2)


# Start the Tkinter event loop
window.mainloop()
