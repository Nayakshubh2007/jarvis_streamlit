import streamlit as st
import datetime
import wikipedia

st.title("Jarvis AI Assistant")

def process_command(command):
    command = command.lower()

    if "time" in command:
        return datetime.datetime.now().strftime("The time is %H:%M")

    elif "youtube" in command:
        return "Open: https://youtube.com"

    elif "google" in command:
        return "Open: https://google.com"

    elif "who is" in command:
        person = command.replace("who is", "")
        try:
            return wikipedia.summary(person, sentences=2)
        except:
            return "Not found"

    elif "what is" in command:
        thing = command.replace("what is", "")
        try:
            return wikipedia.summary(thing, sentences=2)
        except:
            return "Not found"

    else:
        return "I didn't understand that"

command = st.text_input("Enter your command")

if command:
    response = process_command(command)
    st.write(response)
