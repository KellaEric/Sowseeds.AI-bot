import streamlit as st
import speech_recognition as sr
import pyttsx3
import threading
from config import Config
from helpers.llm_helper import chat, stream_parser

# --------------- Page Setup ---------------
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    layout="centered",
    initial_sidebar_state="expanded"
)

# --------------- Custom CSS ---------------

custom_css = f"""
    <style>
        body {{
            background-color: #000000;
            color: white;
        }}
        .stApp {{
            background-color: #000000;
        }}
        .stButton>button {{
            background-color: #f1c40f;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }}
        .stButton>button:hover {{
            background-color: #e67e22;
        }}
        .stTitle, .stHeader, .stSubheader {{
            color: #f1c40f;
        }}
        .stSidebar, .stSidebarContent {{
            background-color: #1a1a1a !important;
            color: white;
        }}
        .block-container {{
            color: white;
        }}
        footer {{
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #fff;
            background-color: #2c3e50;
            font-size: 14px;
        }}
        .icon-title {{
            font-size: 28px;
            padding-right: 10px;
        }}
    </style>
    <footer>
        &copy; 2025 @AI assistance- Developed by Kella Eric
    </footer>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --------------- TTS Engine ---------------
engine = pyttsx3.init()

# --------------- Sidebar Voice Control ---------------
voices = engine.getProperty('voices')
selected_voice = st.sidebar.selectbox("Select Voice", ["Male", "Female"])
voice_speed = st.sidebar.slider("Voice Speed", 100, 300, 150)

if selected_voice == "Male":
    engine.setProperty('voice', voices[0].id)
else:
    engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', voice_speed)

# --------------- Get Voice Input ---------------
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening... Please speak now.")
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            st.error("⏳ Listening timed out.")
            return None
    try:
        user_input = recognizer.recognize_google(audio)
        st.success(f"🧑 You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        st.error("😕 Couldn't understand the audio.")
    except sr.RequestError:
        st.error("🔌 Speech API unavailable.")
    return None

# --------------- Speak Output ---------------
def speak(text):
    def run_tts():
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            st.warning(f"🔊 Voice error: {e}")
    threading.Thread(target=run_tts).start()

# --------------- Main Function ---------------
def main():
    st.title("🤖 " + Config.PAGE_TITLE)
    st.subheader("💡 AI-powered to the next generation to christian faith based")

    # Sidebar Nav
    with st.sidebar:
        st.markdown("## 🔗 Navigation")
        nav_choice = st.radio("Go to:", ["Chat Assistant", "About", "Help", "Contact"])

        if nav_choice == "About":
            st.info("ℹ️ Sosseds AI is a voice-enabled assistant developed by Kella Eric.")
            st.stop()
        elif nav_choice == "Help":
            st.info("🆘 Use voice or text input to interact.")
            st.stop()
        elif nav_choice == "Contact":
            st.info("📧 Email: support@kella's.ai")
            st.info("🌐 Website: www.kella'stech.ai")
            st.stop()

        st.markdown("## 🤖 Model Selection")
        model = st.selectbox('Choose a model:', Config.OLLAMA_MODELS)

    # Chat State
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History
    for message in st.session_state.messages:
        icon = "🧑" if message["role"] == "user" else "🤖"
        with st.chat_message(message["role"]):
            st.markdown(f"{icon} {message['content']}")

    # Voice + Mute
    use_voice = st.button("🎙️ Use Voice Command")
    mute_tts = st.checkbox("🔇 Mute Voice Output", value=False)

    # Input
    user_prompt = get_voice_input() if use_voice else st.chat_input("💬 I'm here to serve you, feel free...")

    # Response
    if user_prompt:
        with st.chat_message("user"):
            st.markdown(f"🧑 {user_prompt}")
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        with st.chat_message("assistant"):
            with st.spinner("🤔 Reasoning..."):
                try:
                    llm_stream = chat(user_prompt, model=model)
                    assistant_reply = ""
                    for chunk in stream_parser(llm_stream):
                        assistant_reply += chunk
                    st.markdown(f"🤖 {assistant_reply}")
                    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
                    if not mute_tts:
                        speak(assistant_reply)
                except Exception as e:
                    error_msg = f"❌ Error during response: {e}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
# Action buttons
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔍 Search Google"):
                search_url = f"https://www.google.com/search?q={user_prompt}"
                st.markdown(f"[Click here to search]({search_url})", unsafe_allow_html=True)
        with col2:
            if st.button("🖼️ Image Search"):
                image_url = f"https://www.google.com/search?tbm=isch&q={user_prompt}"
                st.markdown(f"[Click here for image results]({image_url})", unsafe_allow_html=True)

# --------------- Launch App ---------------
if __name__ == "__main__":
    main()
