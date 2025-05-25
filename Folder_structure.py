import os

# Base project folder
project_name = "rag_streamlit_assistant"

# Folder structure
folders = [
    project_name,
    f"{project_name}/modules",
    f"{project_name}/models",
    f"{project_name}/data"
]

# Files to create with placeholder content
files = {
    "app.py": "# Streamlit main app\n",
    "requirements.txt": "# Add dependencies here\n",
    f"{project_name}/modules/pdf.py": "# PDF loading and splitting logic\n",
    f"{project_name}/modules/rag.py": "# RAG setup with Mistral model\n",
    f"{project_name}/modules/tts.py": "# Text-to-speech (Coqui TTS)\n",
    f"{project_name}/modules/stt.py": "# Speech-to-text (Vosk)\n",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"📁 Created folder: {folder}")

# Create files with placeholder content
for filepath, content in files.items():
    with open(filepath, "w") as f:
        f.write(content)
    print(f"📄 Created file: {filepath}")

print("\n✅ RAG Voice Assistant project structure created!")
