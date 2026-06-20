import streamlit as st
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import os

# Streamlit UI Setup
st.title("🤖 Desktop Alexa Assistant")
st.write("Click the button below to talk to Alexa!")

listener = sr.Recognizer()

# Voice input function modified for Streamlit
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            st.info("Listening... Speak now...")
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            st.success("Processing voice...")
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except Exception as e:
        st.warning("Could not hear or recognize your voice. Please try again.")
    return command

def run_alexa():
    command = take_command()
    if command:
        st.write(f"**You said:** {command}")
        
        if 'play' in command:
            song = command.replace('play', '')
            st.success(f"Playing {song} (Simulated)")
            # Web browser/YouTube server par direct open nahi hoga, isliye sirf text dikha rahe hain
            
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            st.info(f"Current time is {time}")
            
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            st.write(info)
            
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            st.write(f"😂 {joke}")
            
        else:
            st.write("Please say the command again.")

# Streamlit Trigger Button (Instead of While True loop)
if st.button("🎙️ Start Alexa"):
    run_alexa()


