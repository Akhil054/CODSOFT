import pyttsx3                      #pip install pyttsx3
import datetime 
import speech_recognition as sr     #pip install SpeechRecognition
import wikipedia                    #pip install wikipedia 
import webbrowser
import smtplib 

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
          
    speak("I am Jarvis Sir.. How can I help you")

def takeCommand():
    #It takes microphone as input and giver string output
    # It take command and convert to string and lowercase 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again")
        return  "None"
    return query

#def sendEmail(to, content):
    # Has to less secure the email option in gmail account to work this function 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tamgaonkarakhil@gmail.com', 'your-password')
    server.sendmail('tamgaonkarakhil@gmail.com', to, content )


if __name__ == "__main__":
    speak("Hello Akhil How are you")
    wishme() 
    while True:
        query  = takeCommand().lower()

        # logic for excuting task
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace ("Wikipedia", "")
            # result are called by jarvis 
            results = wikipedia.summary(query, sentences =2)
            speak("According to Wikipedia")
            speak(results)

        # query are given to recognize the command given by default by user 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music ' in query:
            webbrowser.open("spotify.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif 'email to Akhil' in query:
            try:
                speak ("What should I say")
                content = takeCommand()
                to = "tamgaonkarakhil@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
    
            except Exception as e :
                print(e)
                speak(" I was not able to send email")            

        elif 'quit' in query:
            exit()
            
        else:
            print("Not valid command")
            