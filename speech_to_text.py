#install SpeechRecognition
#install pyaudio

import speech_recognition as sr

def speech_recog():
    r=sr.Recognizer() #class
    mic=sr.Microphone() #class
    with mic as source:
        print('Please Speak......')

        r.energy_threshold=50                           #when the voice is reached this threshold only correct conversion occurs
        r.adjust_for_ambient_noise(source,duration=1)     #these 2 steps are done for better result, will remove background noise

        audio=r.listen(source)

        try:
            text=r.recognize_google(audio)
            print("You said:",text)

        except:
            print('Did not here anything....Please say again')

speech_recog()