import speech_recognition as sr
import pyttsx3

# create an instance of the Recognizer class
r = sr.Recognizer()


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# capture audio from the microphone
with sr.Microphone() as source:
    print('say something...')
    # wait for a second to let the recognizer
    # adjust the energy threshold based on
    # the surrounding noise level
    r.adjust_for_ambient_noise(source, duration=0.1)
    audio = r.listen(source)

# convert the captured audio to text
try:
    text = r.recognize_google(audio)
    text = text.lower()
    print('you said: ', text)
except sr.UnknownValueError:
    SpeakText('Sorry, I could not understand audio.')

except sr.RequestError as e:
    SpeakText('Could not request results; {0}'.format(e))
