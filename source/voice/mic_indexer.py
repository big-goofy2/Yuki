import sounddevice as sd

def detect_microphones():
    devices = sd.query_devices() # Fetch all available audio devices
    print("Scanning for available microphones...\n")
    mic_found = False
    
    for index, device in enumerate(devices):
        if device['max_input_channels'] > 0:
        
            print(f"Index {index}: {device['name']}")
            print(f" - Sample Rate: {device['default_samplerate']} Hz")
            print(f" - Input Channels: {device['max_input_channels']}\n")
            
            mic_found = True
    if not mic_found:
        print("No input microphones detected.")

detect_microphones()
