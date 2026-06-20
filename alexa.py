import streamlit as st
import pandas as pd
import datetime
import random
import os

# Streamlit Page Config
st.set_page_config(page_title="Alexa Voice Assistant", layout="centered")

st.title("🧠 Alexa Assistant (Streamlit Version)")
st.caption("Text-based Simulation for Cloud Deployment")

# CSV File check (Local path hata diya hai taaki server pe crash na ho)
csv_filename = "alexa_data.csv"

if os.path.exists(csv_filename):
    df = pd.read_csv(csv_filename)
    st.success("Dataset loaded successfully!")
else:
    st.warning(f"Please make sure '{csv_filename}' is uploaded in the same GitHub repository.")

# Actions simulation instead of crashing modules
def run_alexa_text(command):
    command = command.lower()
    
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        return f"Current time is {current_time}"
        
    elif 'joke' in command:
        jokes = [
            "Why do programmers wear glasses? Because they can't C#!",
            "Why did the computer go to the doctor? It had a virus!",
            "Algorithms: Words used by programmers when they don't want to explain what they did."
        ]
        return random.choice(jokes)
        
    elif 'play' in command:
        song = command.replace('play', '')
        return f"Playing {song} on YouTube (Simulated)"
        
    else:
        return "I can process this intent! (Voice & local paths are disabled on Cloud Server)."

# UI Controls (Text based so it never freezes)
st.markdown("### 🎙️ Type your command below")
user_input = st.text_input("What can I do for you?", placeholder="e.g., What is the time? or Tell me a joke")

if st.button("Run Alexa"):
    if user_input:
        response = run_alexa_text(user_input)
        st.info(f"🤖 **Alexa:** {response}")
    else:
        st.warning("Please enter a command first.")
