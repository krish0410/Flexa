# Flexa - Voice assistant
The objective of the project is to create a QnA environment between you and your assistance in real time. It is very much similar to Alexa<br />
Before running code in your system , make sure you should have 4 GB RAM , for smooth loading of Transformer model.<br/>
# Libraries used in the project
from gtts import gTTS<br/>
from playsound import playsound<br/>
import speech_recognition as sr<br/>
import datetime<br/>
import calendar<br/>
from datetime import date<br/>
import pyjokes<br/>
import wikipedia<br/>
import time<br/>
import webbrowser<br/>
import os<br/>
import requests<br/>
import re<br/>
import bs4<br/>
import html2text<br/>
import smtplib <br/>
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline<br/>
