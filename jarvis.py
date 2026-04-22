import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyttsx3
import os

# -------- Text to Speech --------
engine = pyttsx3.init()

def speak(text):
    try:
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass


# -------- Voice Recognition --------
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")

            command = recognizer.recognize_google(audio)
            print("You said:", command)

            return command.lower()

        except:
            return ""


# -------- Command Processing --------
def process_command(command):
    command = command.lower()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        return f"The time is {time}"

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open wikipedia" in command:
        webbrowser.open("https://wikipedia.org")
        return "Opening Wikipedia"

    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp"
    
        # -------- Desktop Apps --------

    elif "open notepad" in command:
        os.startfile("notepad.exe")
        return "Opening Notepad"

    elif "open calculator" in command:
        os.startfile("calc.exe")
        return "Opening Calculator"

    elif "open cmd" in command or "open command prompt" in command:
        os.startfile("cmd.exe")
        return "Opening Command Prompt"

    elif "open paint" in command:
        os.startfile("mspaint.exe")
        return "Opening Paint"

    elif "open vscode" in command or "open visual studio code" in command:
        os.startfile("C:\\Users\\Shubham Nayak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        return "Opening VS Code"

    elif "open chrome" in command:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        return "Opening Chrome"

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook"

    elif "open twitter" in command:
        webbrowser.open("https://twitter.com")
        return "Opening Twitter"

    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        return "Opening Instagram"

    elif "open github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"

    elif "zomato" in command:
        webbrowser.open("https://www.zomato.com")
        return "Opening Zomato"

    elif "amazon" in command:
        webbrowser.open("https://www.amazon.in")
        return "Opening Amazon"

    elif "flipkart" in command:
        webbrowser.open("https://www.flipkart.com")
        return "Opening Flipkart"

    elif "spotify" in command:
        webbrowser.open("https://www.spotify.com")
        return "Opening Spotify"

    elif "netflix" in command:
        webbrowser.open("https://www.netflix.com")
        return "Opening Netflix"

    elif "gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    elif "urban company" in command:
        webbrowser.open("https://www.urbancompany.com")
        return "Opening Urban Company"

    elif "quora" in command:
        webbrowser.open("https://www.quora.com")
        return "Opening Quora"

    elif "swiggy" in command:
        webbrowser.open("https://www.swiggy.com")
        return "Opening Swiggy"

    elif "uber" in command:
        webbrowser.open("https://www.uber.com")
        return "Opening Uber"

    elif "ola" in command:
        webbrowser.open("https://www.olacabs.com")
        return "Opening Ola"

    elif "gemini" in command:
        webbrowser.open("https://gemini.google.com")
        return "Opening Gemini"

    elif "zoom" in command:
        webbrowser.open("https://zoom.us")
        return "Opening Zoom"
    
    elif "poki games" in command:
        webbrowser.open("https://poki.com")
        return "Opening Poki Games"
    
    elif "codeforces" in command:
        webbrowser.open("https://codeforces.com")
        return "Opening Codeforces"
    
    elif "leetcode" in command:
        webbrowser.open("https://leetcode.com")
        return "Opening LeetCode"
    
    elif "hacker rank" in command:
        webbrowser.open("https://www.hackerrank.com")
        return "Opening HackerRank" 
    
    elif "geeksforgeeks" in command:
        webbrowser.open("https://www.geeksforgeeks.org")
        return "Opening GeeksforGeeks"
    
    elif "codepen" in command:
        webbrowser.open("https://codepen.io")
        return "Opening CodePen"
    
    elif "replit" in command:
        webbrowser.open("https://replit.com")
        return "Opening Replit"
    
    elif "stack overflow" in command:
        webbrowser.open("https://stackoverflow.com")
        return "Opening Stack Overflow" 
    elif "classroom" in command:
        webbrowser.open("https://classroom.google.com")
        return "Opening Google Classroom"
    
    elif "drive" in command:
        webbrowser.open("https://drive.google.com")
        return "Opening Google Drive"
    
    elif "maps" in command:
        webbrowser.open("https://maps.google.com")
        return "Opening Google Maps"
    
    elif "news" in command:
        webbrowser.open("https://news.google.com")
        return "Opening Google News"
    
    elif "gpay" in command:
        webbrowser.open("https://pay.google.com")
        return "Opening Google Pay"
    
    elif "photos" in command:
        webbrowser.open("https://photos.google.com")
        return "Opening Google Photos"
    
    

    elif "chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"

    elif "who is" in command:
        person = command.replace("who is", "")
        try:
            return wikipedia.summary(person, sentences=2)
        except:
            return "Sorry, I couldn't find information."

    elif "what is" in command:
        person = command.replace("what is", "")
        try:
            return wikipedia.summary(person, sentences=2)
        except:
            return "Sorry, I couldn't find information."

    elif "exit" in command:
        return "exit"

    else:
        return "I didn't understand that."