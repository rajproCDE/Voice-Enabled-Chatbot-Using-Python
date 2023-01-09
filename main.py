from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
from xyz import convo

engine=pp.init()

def _init_(self, voice=0, volume=1, rate=125):
    self.engine = pp.init()
    self.engine.setProperty("rate", rate)
    self.engine.setProperty("volume", volume)
    voices = self.engine.getProperty("voices")
    self.engine.setProperty("voice", voices[0].id)

voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voices',voices[0].id)
    

def speak(self):
    engine.say(self)
    engine.runAndWait()

#pyttsx3

chatbot = ChatBot('Ron Obvious')


trainer=ListTrainer(chatbot)

#training bot with the help of trainer

trainer.train(convo)

# Window Using Tkinter    

main=Tk()

main.geometry("500x600")

main.title("The ChatBot")
img=PhotoImage(file="retro.png")

photoL=Label(main,image=img)

photoL.pack(pady=5)

def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()

        except Exception as e:
           print(e)
           print("Not Recognized")   
    exit(0)

def ask_from_bot():
    query=textF.get()
    answer_from_bot=chatbot.get_response(query)
    msgs.insert(END,"Your:" + query)
    msgs.insert(END,"Bot:" + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END) 
    msgs.yview(END)

frame=Frame(main)

scb=Scrollbar(frame)

msgs=Listbox(frame,width=80,height=10,yscrollcommand=scb.set)

scb.pack(side=RIGHT,fill=Y)

msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

# Creating the Text field

textF=Entry(main,font=("Verdana",20))

textF.pack(fill=X,pady=10)

# Making the Button

btn1=Button(main,text="Text",font=("Verdana",20),command=ask_from_bot)

btn1.pack(side=LEFT)

#making the mic button
#new added

btn2=Button(main,text="Voice",font=("Verdana",20),command=takeQuery)
btn2.pack(side=RIGHT)


#creating a function

def  enter_function(event):
    btn1.invoke()


#going to bind enter key with enter key

main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()  
         
    

t=threading.Thread(target=repeatL)

t.start()





main.mainloop()