import speech_recognition as sr
from gtts import gTTS
import urllib3
import time
from lxml import html
import requests
import webbrowser
import os
import subprocess

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
from pygame import mixer
mixer.init()
loopme=1

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    #print("Please wait. Calibrating microphone...")
    # listen for 1 second and create the ambient noise energy level
  r.adjust_for_ambient_noise(source, duration=1)
  print("Say something!")
  audio = r.listen(source,phrase_time_limit=5)
 
# recognize speech using Sphinx/Google
try:
  #response = r.recognize_sphinx(audio)
  response = r.recognize_google(audio)
  print("I think you said '" + response + "'")
  tts = gTTS(text="I think you said "+str(response), lang='en')
  tts.save("response.mp3")
  mixer.music.load('response.mp3')
  mixer.music.play()
 # str1="Processing"
  t=response
  if(response.find("play")!=-1):                                                   #Play youtube video
         
          le=t.find("play")+len("play")+1
          t=t[le:]
          print ("Playing",t)
          time.sleep(5)
          str1="Processing"
          obj1=gTTS(str(str1), lang='en')
          obj1.save("Process.mp3")
          mixer.music.load('Process.mp3')
          mixer.music.play()
          q='https://www.youtube.com/results?search_query='+t
          #page = requests.get(q)
          #tree = html.fromstring(page.content)
          #buyers = tree.xpath('//*[@id="results"]/ol[1]/li[1]/ol[1]/li[1]/div[1]')
          #a=buyers[1]
          #p=a.get("data-context-item-id")
          webbrowser.open_new(q)
  elif(t.find("open")!=-1):                                                   # Open windows application
          le=t.find("open")+len("open")+1
          t=t[le:]
          if(t=="calculator" or t=="Calculator"):
              os.system("start calc.exe")
              #mlist.append("calc.exe")
          elif(t=="Notepad" or t=="notepad"):
              os.system("start notepad.exe")
              #mlist.append("notepad.exe")
          elif(t=="Paint" or t=="paint"):
              os.system("start mspaint.exe")
              #mlist.append("mspaint.exe")
          elif((t.find("Google")!=-1) or (t.find("chrome")!=-1)):
              webbrowser.open_new("https://www.google.com/webhp?rlz=1C1RLNS_enIN755IN755&ie=UTF-8&rct=j")
          elif(t.find("computer")!=-1):
              subprocess.Popen(r'explorer /select,"C:\Documents and Settings[user]\Desktop\My Computer"')
  elif(t.find("Google for")!=-1):
          query=t[11:]
          webbrowser.open_new("https://www.google.co.in/search?q="+query)
  elif(t.find("Youtube")!=-1):
          query=t[12:]
          webbrowser.open_new("https://www.youtube.com/results?search_query="+query)
  elif(t.find("hello")!=-1 or t.find("hi")!=-1):
          
          print ("Playing",t)
          time.sleep(2)
          str1="Hello sir how are you this is cheeku your voice assistant"
          obj1=gTTS(str(str1), lang='en')
          obj1.save("hi.mp3")
          mixer.music.load('hi.mp3')
          mixer.music.play()
  



except sr.UnknownValueError:
  
  loopme=0;
  print("I could not understand audio")
except sr.RequestError as e:
  print(" error; {0}".format(e))

