import sounddevice as sd
import soundfile as sf

sample_rate = 16000
duration = 5

print("Speak into your mic...")
recorded_audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="float32")
sd.wait()
print("Recording complete.")

sf.write("recording.wav", recorded_audio, sample_rate) # save it
print(f"Saved to recording.wav")