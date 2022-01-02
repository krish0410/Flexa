#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:21:09 2022

@author: krish
"""

from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

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
                outtext="Ok Krish , we'll meet again"
                myobj = gTTS(text=outtext, lang=language, slow=False)
                myobj.save("temp.mp3")
                playsound("temp.mp3")
                break
            else:
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("temp.mp3")
                playsound("temp.mp3")                
        except:
            outtext="Couldn't get you , Please say again"
            myobj = gTTS(text=outtext, lang=language, slow=False)
            myobj.save("temp.mp3")
            playsound("temp.mp3")
            