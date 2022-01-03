#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:21:09 2022

@author: krish
"""

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from datetime import date
import calendar

# initialize
r = sr.Recognizer()


# Convert Speech to Text in Real time
while True:
    with sr.Microphone() as source:
        # clear background noise
        r.adjust_for_ambient_noise(source, duration=0.3)
        
        print("Speak now")
        # capture the audio
        audio = r.listen(source)
        
        try:
            mytext = r.recognize_google(audio)
            language = 'en'
            if mytext == 'Python please stop':
                outtext="Ok Krish , hope to see you again"
                myobj = gTTS(text=outtext, lang=language, slow=False)
                myobj.save("temp.mp3")
                print("Flexa : ",outtext)
                playsound("temp.mp3")
                break
            elif mytext == 'who are you':
                outtext="I am Flexa !"
                myobj = gTTS(text=outtext, lang=language, slow=False)
                myobj.save("temp.mp3")
                print("Flexa : ",outtext)
                playsound("temp.mp3")
            elif mytext == 'how are you':
                outtext="I am fine , what about you"
                myobj = gTTS(text=outtext, lang=language, slow=False)
                myobj.save("temp.mp3")
                print("Flexa : ",outtext)
                playsound("temp.mp3")
            elif mytext == "what is today's date":
                today = date.today()
                d=today.strftime("%B %d, %Y")
                t="Today is "
                outtext=t+d
                myobj = gTTS(text=outtext, lang=language, slow=False)
                myobj.save("temp.mp3")
                print("Flexa : ",outtext)
                playsound("temp.mp3")
            elif mytext == "what is today's day":
                today = date.today()
                d=calendar.day_name[today.weekday()]
                t="Today is "
                outtext=t+d
                myobj = gTTS(text=outtext, lang=language, slow=False)
                myobj.save("temp.mp3")
                print("Flexa : ",outtext)
                playsound("temp.mp3")
            else:
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("temp.mp3")
                print("Flexa : ",mytext)
                playsound("temp.mp3")                
        except:
            outtext="Couldn't get you , Please say again"
            myobj = gTTS(text=outtext, lang=language, slow=False)
            myobj.save("temp.mp3")
            playsound("temp.mp3")
