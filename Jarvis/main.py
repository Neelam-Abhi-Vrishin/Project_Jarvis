#Importing required libraries
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

r = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
        speak("Opened Google")
    
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com")
        speak("Opened linkedin")
    
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")
        speak("Opened facebook")
    
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opened youtube")
    
    elif "open playstore" in command.lower():
        webbrowser.open("https://play.google.com")
        speak("Opened playstore")
    
    elif "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com")
        speak("Opened instagram")
    
    elif "open x" in command.lower():
        webbrowser.open("https://www.x.com")
        speak("Opened X")
    
    elif "play" in command.lower():
        # plays only praise, faceoff and skyfall songs
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 
        speak("playing music")
    
    elif "shutdown" or "quit" or "exit" or "close" in command.lower():
        speak("Shutting down...")
        return False
    else:
        print("Command cannot be processed. Sorry for the inconvenience.")

# Main function
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    while True:
        # recognize speech using Google Speech Recognition
    
        try:
            with sr.Microphone() as source:
                
                print("Listening for wake word...")
                audio = r.listen(source, timeout = 3, phrase_time_limit = 1)
            
            wk_word = r.recognize_google(audio)
            print(wk_word)
            
            if(wk_word.lower() == "jarvis"):
                speak("Yeah")
                # Listen the user for command
                with sr.Microphone() as source:
                    print("Jarvis Activated...! Waititing for command")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                processCommand(command)
                
        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        
        except Exception as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        