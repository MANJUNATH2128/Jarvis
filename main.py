import speech_recognition as sr
import time
from time import ctime
import playsound
import os
import random
from gtts import gTTS
import webbrowser
import json
from difflib import get_close_matches


r=sr.Recognizer()
def audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            jarvis(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            jarvis('Sorry i did not get that ')
        except  sr.RequestError:
            jarvis('Sorry my speech service is down...')
        return voice_data

def jarvis(audio):
    tts=gTTS(text=audio,lang='en',slow=False)
    r=random.randint(1,1000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio)
    os.remove(audio_file)

def translate(word):
    data=json.load(open(r"C:\Users\Manju\Desktop\Python\Python_projects\Jarvis\data.json"))
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter Y if Yes, or N if No: "%get_close_matches(word,data.keys())[0])
        if yn=='Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=='N':
            return "The word dosen't exist.Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word dosen't exist.Please double check it."

def respond(voice_data):
    if 'what is your name' in voice_data or 'who are you' in voice_data:
        jarvis('My name is jarvis')
    if 'are you there' in voice_data:
        jarvis('Hello sir at yor service')
    if 'how are you' in voice_data:
        jarvis('I am fine Sir, how are you')
    if 'fine' in voice_data:
        jarvis('Thats great sir')
    if 'what time is it' in voice_data:
        jarvis(ctime())
    if 'search' in voice_data:
        search=audio('What do you want to search for..')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        jarvis('Here is what i found for '+search)
    if 'location' in voice_data:
        location=audio('What is the location')
        url='https://google.nl/maps/place/'+location+'/&amp'
        webbrowser.get().open(url)
        jarvis('Here is the location of '+location)
    if 'meaning' in voice_data:
        word1=audio('What is the word..')
        word=translate(word1)
        if type(word)==list:
            for i in word:
                jarvis(i)
            jarvis('These are the meaning')
        else:
            jarvis(word)
    if 'youtube' in voice_data:
        jarvis('opening youtube..')
        url='https://www.youtube.com'
        webbrowser.get().open(url)
    if 'exit' in voice_data or 'close' in voice_data:
        jarvis('Closing the app...')
        exit()
    
time.sleep(1)
jarvis('Hello Sir how can i help you..')
while(1):
    voice_data=audio()
    respond(voice_data)