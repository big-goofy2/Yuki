import whisper

model = whisper.load_model("base") # load model
result = model.transcribe("recording.wav",fp16=False) # transcribe an audio file
print(result["text"])
