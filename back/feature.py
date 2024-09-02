import os
from back.command import speak
from back.config import Name
import pywhatkit as kit
import re
import webbrowser
import sqlite3
import pvporcupine
import pyaudio
import struct
import time
from back.test import remove
import pyautogui
import subprocess
from pipes import quote
from hugchat import hugchat

patch=sqlite3.connect("charlie.db")
cursor=patch.cursor()
model_path="back\\charlie\\charlie.ppn"
access_key = 'V6vdrqpPlHn9DyQV4XwrB+Wtj+gcyx+FYyA6+wr7fbHGHWdxsqF8UA=='




def open(query):
    query=query.replace(Name,"")
    query=query.replace("open","")
    query.lower
    app=query.strip()
    if app!="":
        try:
            cursor.execute(
                "SELECT path FROM sys_command WHERE name IN(?)",(app,))
            results = cursor.fetchall()

            if len(results)!=0:
                speak("opening"+query)
                os.startfile(results[0][0])

            elif len(results)==0:
                cursor.execute("SELECT url FROM web_command WHERE name IN (?)", (app,))
                results=cursor.fetchall()

                if len(results)!=0:
                    speak("Opennig"+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("opening"+query)
                    try:
                        os.system("start"+query)
                    except:
                        speak("sorry"+query+"not found")
        except:
            speak("something went wrong")


def play(query):
    search=extract(query)
    speak("playing "+search+" on Youtube")
    kit.playonyt(search)

def extract(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None


def hotword():
    access_key = 'V6vdrqpPlHn9DyQV4XwrB+Wtj+gcyx+FYyA6+wr7fbHGHWdxsqF8UA=='
    model_path = 'C:\\Users\\12345\\Downloads\\charlie_en_windows_v3_0_0\\charlie.ppn'


    try:
        porcupine = pvporcupine.create(
            access_key=access_key,
            keyword_paths=[model_path]  # Path to your "Charlie" .ppn file
        )
        print("Porcupine initialized successfully.")
    except Exception as e:
        print("Error initializing Porcupine:", e)
        return
    
    try:
        aud = pyaudio.PyAudio()
        stream = aud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
    except Exception as e:
        print("Error initializing audio stream:", e)
        return

    print("Audio stream initialized successfully.")
    
    try:
        while True:
            keyword = stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            keyword_index = porcupine.process(keyword)
            if keyword_index >= 0:
                print("Hotword 'Charlie' detected")
                import pyautogui as gui
                gui.keyDown("win")
                gui.press("j")
                time.sleep(2)
                gui.keyUp("win")
    except Exception as e:
        print("Error during hotword detection:", e)
    finally:
        if stream:
            stream.stop_stream()
            stream.close()
        if aud:
            aud.terminate()

def contact(query):
    words_to_remove = [Name, 'make', 'a', 'to','voice', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile = str(results[0][0])
        if not mobile.startswith('+91'):
            mobile = '+91' + mobile

        return mobile, query
    except:
        speak('This contact does not exist')
        return 0, 0
def whatsApp(mobile_no, message, note, name):

    if note == 'message':
        target_tab = 12
        prompt = "message sent successfully to "+name

    elif note == 'voice call':
        target_tab = 7
        message = ''
        prompt = " voice calling to "+name

    else:
        target_tab = 6
        message = ''
        prompt = "staring video call with "+name
    new = quote(message)
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={new}"
    begin  = f'start "" "{whatsapp_url}"'
    subprocess.run(begin , shell=True)
    time.sleep(4)
    subprocess.run(begin , shell=True)
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(prompt)

def chatBot(query):
    user = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="back\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user)
    print(response)
    speak(response)
    return response
