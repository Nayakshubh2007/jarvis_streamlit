import streamlit as st
import datetime
import wikipedia
import pytz

st.set_page_config(page_title="Jarvis AI", layout="centered")

st.title("Narrow AI Assistant 🤖")

# -------- Time Function --------
def get_time():
    india = pytz.timezone("Asia/Kolkata")
    return datetime.datetime.now(india).strftime("%I:%M %p")

# -------- Command Processing --------
def process_command(command):
    command = command.lower()

    if "time" in command:
        return f"The time is {get_time()}"

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

# -------- Chat Memory --------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------- Display Messages --------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------- Input Box --------
user_input = st.chat_input("Type your message...")

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # generate response
    response = process_command(user_input)

    # show assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)
