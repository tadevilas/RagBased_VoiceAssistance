# RagBased_VoiceAssistance
This Project use Rag Based Voice Assistance system
# 🎙️ RAG Voice Assistant with Whisper & Mistral

This is an open-source, fully local **voice assistant** that can:

- Take your voice input
- Transcribe it using [Whisper](https://huggingface.co/openai/whisper-base)
- Search through a PDF using a RAG pipeline
- Generate accurate answers using [Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
- Convert the response to speech using [Coqui TTS](https://github.com/coqui-ai/TTS)

All done using **free and open-source tools** — no internet-based APIs required!

---

## 🚀 Features

- 🔊 Voice input using `Whisper` via Hugging Face
- 📄 PDF ingestion + chunking
- 📚 RAG-based question answering with `FAISS` + `Mistral-7B`
- 🗣️ Text-to-speech with `Coqui TTS`
- 🧠 Fully local (can run offline after models are downloaded)
- 💡 Streamlit interface

---

## 🗂️ Project Structure

