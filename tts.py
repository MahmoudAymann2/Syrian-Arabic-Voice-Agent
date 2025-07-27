from google.cloud import texttospeech
import os

def synthesize_speech(text):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="ar-XA",
        name="ar-XA-Wavenet-D"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    audio_path = "response.mp3"
    with open(audio_path, "wb") as out:
        out.write(response.audio_content)

    return audio_path
