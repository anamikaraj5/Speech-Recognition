import pyttsx3
text_sp=pyttsx3.init()
# text=input('Enter any text....\n')
voices=text_sp.getProperty('voices')
for voice in voices:
    print('ID',voice.id)
text_sp.setProperty('voice',voices[1].id)
text_sp.say(text)
text_sp.runAndWait()

