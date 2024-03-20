import whisper

model = whisper.load_model("base")

result = model.transcribe("")

result["text"][:300]
