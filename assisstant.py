import speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import datetime
import pytz
import wikipedia
from wikipedia.wikipedia import search
# from newsfetch.news import newspaper
import feedparser
import json
import re
import news

with open('toi_feed_links.json', 'r') as myfile:
    data = myfile.read()
feed_links = json.loads(data)

listener = sr.Recognizer()
#for index, name in enumerate(sr.Microphone.list_microphone_names()):
  #  print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
engine = pyttsx3.init()
voices = engine.getProperty('voices')
newVoiceRate = 140
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice',voices[1].id)



# def talk(text):
#     print(text)
#     engine.say(text)
#     engine.runAndWait()
    


def give_command():
    try:
        with sr.Microphone(device_index=3) as source:
            print('listening...')
            command=''
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
                
            
    except:
        pass
    return command


def give_sec_command():
    try:
        with sr.Microphone(device_index=3) as source:
            print('listening...')
            sec_command=''
            voice = listener.listen(source)
            sec_command = listener.recognize_google(voice)
            sec_command = sec_command.lower()
            print(sec_command)            
    except:
        pass
    return sec_command


def run_alexa(command):
    
    
            

    
    if 'play' in command:
        song  = command.replace('play','')
        word = 'playing' + song
        msg = word
        # print(word)
        kt.playonyt(song)
    
    elif 'time' in command:
        
        ti = datetime.datetime.now().strftime('%I:%M:%p')
        
        msg = 'The time right now is' + ti 
    
    # elif 'who is' or 'give info on' in command:
    #     person = command.replace('who is','')
    #     person = command.replace('info on','')
    #     data = wikipedia.summary(person,1)
    #     print("From Wikipedia:")
    #     print(data)
    #     talk(data)

    elif 'search on google' in command:
        sear = command.replace('search on google','')
        kt.search(sear)

    
    elif 'news' in command:
        msg = news.news(command)
          
    
    
    

    elif 'who is' in command:
        person = command.replace('who is','')
        person = command.replace('info on','')
        data = wikipedia.summary(person,1)
        print("From Wikipedia:")
        print(data)
        msg = data

    else:
        msg = "Have a great day"
    return msg
        
if __name__ == "__main__":
    command = give_command()
    run_alexa(command)


