import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening... Speak now:")
    audio = recognizer.listen(source)    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")
    except sr.RequestError:
        print("Error connecting to Google Speech Recognition API")