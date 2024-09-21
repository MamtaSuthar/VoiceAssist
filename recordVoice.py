import soundfile as sf
import wave
import numpy as np
from scipy.spatial.distance import cosine
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    with open("kavir", "wb") as f:
        f.write(audio.get_wav_data())



def record_voice_sample(file_name):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak the voice sample.")
        audio = r.listen(source)

    # Save the audio to a file
    with wave.open(file_name, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
        f.writeframes(audio.get_raw_data())


def match_user_voice(file_name):
    r = sr.Recognizer()

    # Load the stored voice sample
    stored_sample, sr_stored = sf.read(file_name)

    with sr.Microphone() as source:
        print("Please speak and I will compare your voice with the stored sample.")
        audio = r.listen(source)

    user_sample = np.array(audio.get_raw_data(), dtype=np.float32)


    similarity = 1 - cosine(stored_sample, user_sample)

    if similarity > 0.5:
        print("Voice match found! Similarity: {:.2f}".format(similarity))
    else:
        print("No voice match found. Similarity: {:.2f}".format(similarity))

stored_sample_path = "stored_sample.wav"

# Uncomment the following line to record and store a voice sample
record_voice_sample(stored_sample_path)


match_user_voice(stored_sample_path)