
import whisper
import tempfile

model = whisper.load_model("base")

def transcribe_audio(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path, language="hi", fp16=False)
    return result["text"]
