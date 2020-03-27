import speech_recognition as SR

R = SR.Recognizer()

with SR.Microphone() as source:
    print("Di algo: ")
    audio = R.listen(source)

    try:
        text = R.recognize_google(audio, language='es-MX')
        print("Has dicho: {}".format(text))
    except:
        print("No te entiendo")