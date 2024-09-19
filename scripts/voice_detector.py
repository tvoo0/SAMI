import speech_recognition as sr
import pyttsx3 as tts
import datetime

voice_detection = sr.Recognizer()
SAMI = tts.init()

def speak(text, rate = 250):
    SAMI.setProperty('rate', rate)
    SAMI.say(text)
    SAMI.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour <= 12:
        print("Good Morning! How may I assist you today?")
        speak("Good Morning! How may I assist you today?")
    elif hour > 12 and hour < 5:
        print("Good Afternoon! How may I assist you today?")
        speak("Good Afternoon! How may I assist you today?")
    else:
        print("Good Evening! How may I assist you today?")
        speak("Good Evening! How may I assist you today?")

def bot_run():
    with sr.Microphone() as voice_input:
        print('I am listening.....')
        voice = voice_detection.listen(voice_input)
        voice_detection.adjust_for_ambient_noise(voice_input, duration=1)
        try:
            command = voice_detection.recognize_google(voice, language='en_gb')
            command = command.lower()
            print(f'User: {command}')
            print('Interpreting...')
        except Exception as exception:
            print('AI: I did not quite catch that. Can you please try again?')
            speak('I did not quite catch that. Can you please try again')
            return 'None'
    return(command)

