import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess as sp
import os
import random
import cv2
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def takecommand(ask=""):

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening')
		talk('Listening')

		r.pause_threshold = 0.5
		audio = r.listen(source)

		try:
			print("Recognizing")
			talk("Recognizing")
			command = r.recognize_google(audio, language='en-in')
			print(command)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			talk("say that again sir")
			main()
    		#return "None"
		
		return command

def askname():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("what is your name")
        talk('what is your name')
        speak = r.listen(source)
    
    try :
        name = r.recognize_google(speak, language = 'en-in')
        l=["mahitha" ,"sowmya" ,"soumya" ,"sawmya","mahi","mahita"]
        lname=list(name.split())
        for i in lname:
            if(i.lower() in l):
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour <12:
                    print("good morning " + i)
                    talk("good morning " + i)
                elif hour>=12 and hour<18:
                    print("good afternoon " + i)
                    talk("good afternoon " + i)
                else:
                    print("good Evening " + i)
                    talk("good Evening " + i)

                print('what can i do for you')
                talk('what can i do for you')
                return
        
        print("incorrect name")
        talk("incorrect name")
        quit()
    except Exception as e:
        print("Say that again please...")
        talk("Say that again please")
        askname()
    
def main():
    while True:
        command=takecommand()
        print(command)
        #youtube video
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        #your name
        elif 'your name' in command:
            print('my name is levi')
            talk('my name is levi')
        #time
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            talk('Current time is ' + time)
        #wikipedia
        elif 'definition of' in command:
            try:
                defi,of,person = command.split()
                info = wikipedia.summary(person,1)
                print(info)

                talk(info)
            except:
                print('sorry could not find information')
                talk('sorry could not find information')
        #random music
        elif 'music' in command:
            music_dir ="C:\\Users\\saima\\OneDrive\\Desktop\\songs"
            files = os.listdir(music_dir)
            music = random.choice(files)
            os.startfile(os.path.join(music_dir, music))
            
        #day
        elif 'day' in command:
            day = datetime.datetime.today().weekday() +1
            Day_dict = {1: 'Monday', 2: 'Tuesday',3: 'Wednesday', 4: 'Thursday',5: 'Friday', 6: 'Saturday',7: 'Sunday'}
            if day in Day_dict.keys():
                dayw = Day_dict[day]
                print(dayw)
                talk("The day is " + dayw)
        #spotify song
        elif 'song' in command:
            search = command.replace('song', '')
            url="https://open.spotify.com/search/"+search
            webbrowser.get().open(url)
            talk("You are listening to"+ search+"enjoy sir")
        #how are you
        elif 'how are you' in command:
            print('I am fine')
            talk('I am fine ')
        #weather
        elif "weather" in command:
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            talk("Here is what I found for on google")
        #joke
        elif 'joke' in command:
            p=pyjokes.get_joke()
            print(p)
            talk(p)
        #notepad
        elif 'notepad' in command:
            print('opening notepad')
            talk('opening notepad')
            sp.call("Notepad.exe")
        #calculator
        elif 'calculator' in command:
            print('opening calculator')
            talk('opening calculator')
            sp.call("calc.exe")
        #command prompt
        elif 'command prompt' in command:
            print('opening command prompt')
            talk('opening command prompt')
            sp.call("cmd.exe")
        #search for anything    
        elif "search" in command:
            try:
                command = command.replace('search', '')
                pywhatkit.search(command)
                print("Searching")
                talk("searching"+command)
            except:
                print("sorry,unable to find the information")
                talk("sorry,unable to find the information")
        #open any website
        elif 'open' in command:
            open,command=command.split()
            print('opening',command)
            talk('opening'+command)
            webbrowser.open("www."+command+".com")
        #whatsapp
        elif 'whatsapp' in command.lower():
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().strftime('%M'))
            pywhatkit.sendwhatmsg('+918688231814','hiee',hour,minute+1)
            pass
        #selfie
        elif 'selfie' in command.lower():
            cap = cv2.VideoCapture(0)
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
            while True:
                _, frame = cap.read()
                original_frame = frame.copy()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = face_cascade.detectMultiScale(gray, 1.3, 5)
                for x, y, w, h in face:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    face_roi = frame[y:y+h, x:x+w]
                    gray_roi = gray[y:y+h, x:x+w]
                    smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
                    for x1, y1, w1, h1 in smile:
                        cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                        file_name = f'yoo-{time_stamp}.png'
                        cv2.imwrite(file_name, original_frame)
                cv2.imshow('cam star', frame)
                if cv2.waitKey(10) == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        #exit
        elif 'exit' or 'stop' or 'quit' in command:
            quit()
        
        else:
            talk('Please say the command again.')
print('hi i am levi your desktop assistant')
talk('hi i am levi your desktop assistant')
#askname()
main()
