# Streamlit main app
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from modules.pdf import load_pdf
from modules.rag import setup_rag
from modules.stt import speech_to_text
from modules.tts import text_to_speech

def main():
    st.title("🎙️ RAG Voice Assistant with Whisper & Mistral")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file:
        docs = load_pdf(uploaded_file)
        rag_chain = setup_rag(docs, model_name="mistralai/Mistral-7B-Instruct-v0.1")

        if st.button("🎤 Record and Ask"):
            query = speech_to_text(duration=5)
            st.write(f"Recognized: **{query}**")

            with st.spinner("Generating answer..."):
                answer = rag_chain.run(query)
            st.write(f"**Answer:** {answer}")

            # Optionally play TTS audio
            audio_path = text_to_speech(answer)
            audio_bytes = open(audio_path, "rb").read()
            st.audio(audio_bytes, format="audio/wav")

if __name__ == "__main__":
    main()
