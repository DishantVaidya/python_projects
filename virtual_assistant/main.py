import speech_recognition as sr   # For speech recognition (converting voice to text)
import pyttsx3                    # For text-to-speech (making the assistant speak)
import webbrowser                 # For opening web pages
import musicLibrary               # Custom module that stores music links (a dictionary expected)
from datetime import datetime     # For getting current date and time
import pyjokes                    # For getting jokes 

# Initialize recognizer and speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to make nova speak aloud
def speak(text):
    print("nova:", text)         # Display spoken text in console
    engine.say(text)              # Convert text to speech
    engine.runAndWait()           # Wait until speaking is finished

# Function to process user commands
def process(c):
    # Open different websites based on command
    if "open google" in c.lower():
        webbrowser.open("www.google.com")
        speak("Opening google")
    elif "open linkedin" in c.lower():
        webbrowser.open("www.linkedin.com")
        speak("Opening linkedin")
    elif "open youtube" in c.lower():
        webbrowser.open("www.youtube.com") 
        speak("Opening youtube")   
    elif "open facebook" in c.lower():
        webbrowser.open("www.facebook.com")
        speak("Opening facebook")
    elif "open instagram" in c.lower():
        webbrowser.open("www.instagram.com")
        speak("Opening instagram")

    # Play song command (expects song name after the word 'play')
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            speak(f"Playing {song}")
        else:
            speak("Sorry, I couldn't find that song.")

    # Tell current time
    elif "current time" in c.lower():
        current_time = datetime.now().strftime("%I:%M %p")    
        speak(f"Current time is {current_time}")

    # Tell today's date
    elif "date today" in c.lower():
        date = datetime.now().strftime("%A, %d %B %Y")    
        speak(f"Today's date is {date}")

    #Help section
    elif "help" in c.lower():
        speak("I can open websites, play songs, tell time, tell date, tell weather or funny jokes for you.")

    #Tell a joke    
    elif "joke" in c.lower():
        speak(pyjokes.get_joke())

    #Tell current weather
    elif "weather" in c.lower():
        city = "mumbai"  # or extract from speech
        webbrowser.open(f"https://www.google.com/search?q=weather+{city}")
        speak(f"Here's the weather for {city}")
    

# Main program starts here
if __name__ == "__main__":
    speak("Systems ready. nova standing by...")   # Greeting message when program starts

    while True:
        # Listen for the wake word ("nova") or "stop" command
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)               # Capture audio input

        try:
            word = r.recognize_google(audio)       # Convert speech to text
            print("You:", word)

            # If user says "nova", activate assistant
            if "nova" in word.lower():
                speak("Hello, how can I help you?")

                # Listen for next command after wake word
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process(command)               # Execute the recognized command

            # Stop the assistant if user says "stop"
            elif "stop" in word.lower():
                speak("Goodbye!")
                break

            # If no recognized keyword, keep listening
            else:
                print("Listening...")

        # Handle unrecognized speech
        except sr.UnknownValueError:
            print("Didn't catch that.")
        # Handle other unexpected errors
        except Exception as e:
            print(e)
