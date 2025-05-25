# Speech-to-text (Vosk)

import whisper
import sounddevice as sd
import wavio
import tempfile

# Load Whisper model once globally to save time
model = whisper.load_model("base")

def record_audio(duration=5, fs=16000):
    print("🎤 Recording audio...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return recording, fs

def speech_to_text(duration=5):
    recording, fs = record_audio(duration)
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmpfile:
        wavio.write(tmpfile.name, recording, fs, sampwidth=2)
        print(f"🎤 Audio saved to {tmpfile.name}, transcribing...")
        result = model.transcribe(tmpfile.name)
    return result["text"]
