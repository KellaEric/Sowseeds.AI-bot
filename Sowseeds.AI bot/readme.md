3. System Architecture
3.1 Frontend (UI Layer)
The frontend is developed with Streamlit, a Python-based open-source library designed for building and sharing data web apps [2]. It provides an intuitive and reactive interface with minimal coding overhead.

3.2 Voice Interaction
The application uses:

pyttsx3 for TTS conversion, allowing voice customization [3].

speech_recognition (planned for future) for audio-to-text support [4].

3.3 Backend Processing
The assistant connects to a local LLM instance using Ollama, which supports models like LLaMA and Mistral for privacy-respecting AI deployment [5].

3.4 Navigation and Features
Modules include:

Chat Assistant

About Section

Help and Contact These are routed through a sidebar in the UI with a dark-themed CSS override.

4. Key Features
🎤 Voice Output via pyttsx3

⚙️ Speech Speed Control (100–300 wpm)

📖 Faith-based Language Modeling using Ollama

🎨 Dark Theme UI for readability

🔁 Modular Chat System through llm_helper.py

5. Use Cases
Spiritual Companion: Devotionals, prayers, and biblical encouragement.

Faith Counseling: Guidance in everyday decisions.

Educational Aid: Scripture-based conversations for children and learners.

Church Outreach Tool: Helping churches provide automated support.

![WhatsApp Image 2025-04-07 at 18 55 31_a237299d](https://github.com/user-attachments/assets/3c6ff9ce-d3a4-457f-87b0-64f9d3fec292)
![WhatsApp Image 2025-04-07 at 18 58 08_ff2bcc13](https://github.com/user-attachments/assets/372910d1-86c6-4246-b47f-2f979704fe9a)


![WhatsApp Image 2025-04-07 at 18 59 49_208e6aee](https://github.com/user-attachments/assets/53387669-95f8-4de9-9fa9-0179a224956b)
![{F5C6CFEC-914C-4851-89B7-1CC35A49E91C}](https://github.com/user-attachments/assets/f6654198-ce41-4857-a3e4-80b31e391ea2)
![{A4C9F18F-63F0-4332-8D1F-F92AB1D54ED9}](https://github.com/user-attachments/assets/cd7a43fd-826d-4d88-a79b-fb7d78ed099c)




🚀 How to Run the Sowseeds AI Assistant Locally
This guide walks you through setting up and running the Sowseeds AI Assistant — a voice-enabled, Christian-faith-based AI chatbot developed by Kella Eric using Streamlit, Ollama, and Python.

📁 Project Structure
css
Copy
Edit
Sowseeds.AI.Bot/
│
├── helpers/
│   ├── __init__.py
│   └── llm_helper.py
├── config.py
├── firebase/
├── img.png
├── LICENSE
├── ollama_chatbot.py       # 🧠 Main app script
├── readme.md
├── requirements.txt
└── .gitignore
🛠 Prerequisites
Ensure you have the following installed:

Python 3.10+

Streamlit

Ollama (for running LLMs locally)

Git

🧪 Installation Steps
Clone the Repository


git clone https://github.com/KellaEric/Sowseeds.AI.Bot.git
cd Sowseeds.AI.Bot
Create a Virtual Environment (optional but recommended)


python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On macOS/Linux
Install Dependencies


pip install -r requirements.txt
⚙️ Running the App
Make sure Ollama is running and the required model is installed (e.g., llama3 or another supported one):


ollama run llama3
Then, in your terminal:


streamlit run ollama_chatbot.py
🌐 Access the App
Once launched, you’ll see output like:


Local URL: http://localhost:8501
Open that URL in your browser to interact with the chatbot interface.

🧠 Features
🔊 Voice-enabled interaction using speech_recognition and pyttsx3

✝️ Christian faith-based messaging and recommendations

💬 Streamlit frontend with customizable sidebar

🧩 Modular LLM support via llm_helper.py

🖼️ Simple dark-mode UI with CSS customization

🙏 Author
Developed by Kella Eric




### Getting Starter Project Code

Run the command below to clone the starter project.

```
git clone --single-branch --branch starter_project https://github.com/KellaEric/Streamlit-Ollama-Chatbot.git
```

### Chatbot Features include:
- Ability to select different Ollama models to be used by the chatbot
- Streaming output when responding to users like ChatGPT

### Ollama 
<a href="https://ollama.com/download">Download ollama</a>

### Ollama Commands

#### Start Ollama Server
```
ollama serve
```

#### Run Ollama Model
```
ollama run <model_name>
```

```
ollama run llama2-uncensored
```

#### Download Ollama Model
```
ollama pull <model_name>
```

```
ollama pull llama2-uncensored
```

#### List Installed Ollama Models
```
ollama list
```

#### Delete Installed Ollama Models
```
ollama rm <model_name>
```

```
ollama rm llama2-llama3.2
```
