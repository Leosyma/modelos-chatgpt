
# 🤖 Chatbot with OpenAI and Streamlit

## 📌 Summary

This project is a multi-interface AI chatbot powered by OpenAI's GPT models. It supports voice and text interactions, file analysis (PDF, CSV), image understanding via GPT-4 Vision, function calling for structured output, and web deployment using Streamlit.

---

## 🧠 Project Overview

The chatbot integrates multiple OpenAI functionalities to act as a flexible assistant for real-time communication and intelligent automation.

---

## 🚀 Functionalities

### 1. **Voice Assistant (Speech Recognition & TTS)**
- Captures microphone input using `speech_recognition`.
- Transcribes using `Whisper-1` and responds using GPT-3.5.
- Converts response to audio using OpenAI TTS (`tts-1`) and plays it.

📁 `chatbot_reconhecimento_fala.py`

### 2. **Command-Line Chat with Streaming**
- Simple CLI interface for interactive conversations.
- Maintains conversation history.
- Streams assistant responses in real-time.

📁 `criar_interface_openai.py`

### 3. **Streamlit Web Interface**
- Web app for uploading files and interacting with OpenAI Assistants API.
- Displays messages and responses in real-time.
- Manages uploaded documents and user context.

📁 `projeto_finalizado.py`

### 4. **Assistant with File Upload (PDF/CSV)**
- Uploads documents and assigns them to OpenAI Assistants.
- Performs contextualized queries on documents.
- Uses assistant threading and polling for response delivery.

📁 `assistants_pdf_openai.ipynb`, `assistants_dados_openai.ipynb`

### 5. **Image Analysis with GPT-4 Vision**
- Uploads and queries images.
- Uses GPT-4 Vision to generate image captions and perform object reasoning.

📁 `gpt_vision.ipynb`

### 6. **Text-to-Speech Conversion**
- Generates MP3 audio from text with OpenAI's TTS API.
- Streams or saves audio using `playsound`.

📁 `criacao_audio.ipynb`

### 7. **OpenAI Function Calling**
- Demonstrates how to define functions and receive structured outputs from GPT using `function_call`.
- Integrates with JSON schemas for structured response parsing.

📁 `implementando_funcao_openai.ipynb`

---

## 📦 Libraries and Tools Used

- `openai`
- `streamlit`
- `speechrecognition`
- `playsound`
- `dotenv`
- `PyMuPDF`, `csv`, `re`, `pandas`
- `json`, `time`, `io`, `os`

---

## 🛠️ Requirements

- Python 3.9+
- OpenAI API key (.env file)
- Microphone & Speaker for voice interaction
- Streamlit for web app (optional)

---

## 📂 File Structure

```
├── projeto_finalizado.py
├── chatbot_reconhecimento_fala.py
├── criar_interface_openai.py
├── implementando_funcao_openai.ipynb
├── assistants_pdf_openai.ipynb
├── assistants_dados_openai.ipynb
├── gpt_vision.ipynb
├── criacao_audio.ipynb
├── utils_openai.py
├── utils_files.py
```

---

## ▶️ How to Run

1. Install requirements: `pip install -r requirements.txt`
2. Add your `.env` file with the OpenAI API key.
3. Run the module of interest, e.g.:
   ```bash
   streamlit run projeto_finalizado.py
   ```
4. For voice: `python chatbot_reconhecimento_fala.py`
