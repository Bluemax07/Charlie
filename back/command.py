import pyttsx3
import speech_recognition as sr
import eel
import time



def speak(c):
    c=str(c)
    engine = pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    engine.setProperty("rate",170)
    eel.Display(c)
    engine.say(c)
    eel.receiverText(c)
    engine.runAndWait()


def order():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.Display('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.Display('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        eel.Display(query)
        time.sleep(2)
    except Exception as e:
        return ""
    
    return query.lower()
@eel.expose
def all(message=1):
    
    if message == 1:
        query = order()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from back.feature import open
            open(query)
        elif "on youtube" in query:
            from back.feature import play
            play(query)
        elif "send message" in query or "voice call" in query or "video call" in query:
            from back.feature import contact, whatsApp
            message = ""
            contact_no, name = contact(query)
            if(contact_no != 0):

                if "send message" in query:
                    message = 'message'
                    speak("what message do you want to send")
                    query = order()
                    
                elif "voice call" in query:
                    message = 'voice call'
                else:
                    message = 'video call'
                    
                whatsApp(contact_no, query, message, name)
        else:
            from back.feature import chatBot
            chatBot(query)
            

    except:
        print("error")
    eel.ret()
     
 
    

