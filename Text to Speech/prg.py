import pyttsx3

engine = pyttsx3.init()

# Set the speech rate (speed)
engine.setProperty('rate', 250)  # You can set any value, the default is 200

# Set the volume (0.0 to 1.0)
engine.setProperty('volume', 0.8)  # You can set any value, the default is 1.0

# Set the voice (optional)
# You can get the list of available voices using engine.getProperty('voices')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)  # Select the first voice in the list
# Convert text to speech
text = "Hello, world!"

engine.say(text)
engine.runAndWait()
