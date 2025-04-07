"""
Original Author: Kella Eric
https://www.youtube.com/@kella
"""

import ollama
import speech_recognition as sr
import pyttsx3
from config import Config

# Initialize TTS engine
engine = pyttsx3.init()
system_prompt = Config.SYSTEM_PROMPT

# Function to handle chat with the LLM
def chat(user_prompt, model):
    stream = ollama.chat(
        model=model,
        messages=[
            {'role': 'assistant', 'content': system_prompt},
            {'role': 'user', 'content': f"Model being used is {model}. {user_prompt}"}
        ],
        stream=True,
    )
    return stream

# Function to process streamed LLM response
def stream_parser(stream):
    for chunk in stream:
        if 'message' in chunk and 'content' in chunk['message']:
            yield chunk['message']['content']


# Function to get voice input
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak now.")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("Speech Recognition API is unavailable.")
    return None

# Function to read out responses
def speak(text):
    engine.say(text)
    engine.runAndWait()
