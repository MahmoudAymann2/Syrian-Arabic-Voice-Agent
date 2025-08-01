import whisper

model = whisper.load_model("medium")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path, language="ar")
    return result["text"]
