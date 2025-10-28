import speech_recognition as sr
import pyttsx3

# Initialize recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Robin:", text)
    engine.say(text)
    engine.runAndWait()

def process():
    pass

if __name__ == "__main__":
    speak("Initializing Robin...")
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            start = r.recognize_google(audio)
            print("You said:", start)

            if "robin" in start.lower():
                speak("Hello, how can I help you?")

                #ask for user command
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process()

            elif "stop" in start.lower() :
                speak("Goodbye!")
                break
            else:
                print("Listening...")

        except sr.UnknownValueError:
            print("Didn't catch that.")
        except Exception as e:
            print(e)
