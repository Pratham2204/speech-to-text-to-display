import speech_recognition as sr
import keyboard
import pyaudio

def listen_and_recognize():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Please hold the spacebar to talk...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise once

        # Start recording if the spacebar is pressed
        keyboard.wait('space')
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=10)  # Adjust time limit for your needs

    # Recognize speech using Google Web Speech API 
    try:
        print("Processing speech...")
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        with open('../speech-to-text/op.txt', 'a') as f:
            f.write(text + '\n')
        f.close()
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

if __name__ == "__main__":
    while True:
        listen_and_recognize()
