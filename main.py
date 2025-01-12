import pyttsx3 as pp
import speech_recognition as s
import threading
from tkinter import *
from PIL import Image, ImageTk

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

responses = {
    'hello': 'Hi there!',
    'what is your name?': 'My name is Chatbot, I am created by Sahazad',
    'how are you?': 'I am doing great these days, thanks for asking!',
    'thank you': 'You are welcome!',
    'In which city you live?': 'I live in Bnagalore',
    'In which language you talk?': 'I mostly talk in English',
    'who are you?': 'I am a chatbot created by Sahazad to assist you.',
    'what can you do?': 'I can chat with you, answer your questions, and entertain you!',
    'bye': 'Goodbye! Have a great day!',
    'how old are you?': 'I am timeless! I don\'t age like humans.',
    'what is your purpose?': 'My purpose is to assist you with any queries you may have.',
    'what is the weather like?': 'I am not connected to the internet, but you can check your local weather app for updates!',
    'what time is it?': 'I don’t have access to the current time, but you can check your device!',
    'can you sing?': 'I can’t sing, but I can chat with you all day long!',
    'tell me a joke': 'Why don’t skeletons fight each other? They don’t have the guts!',
    'what is your favorite color?': 'I like all colors equally, but I think blue is nice!',
    'do you like dogs?': 'I think dogs are great! They are loyal and friendly.',
    'do you like cats?': 'Cats are pretty cool, too! They are independent and curious.',
    'what is your favorite food?': 'I don’t eat food, but I think pizza sounds amazing!',
    'are you smart?': 'I try to be as smart as I can! I’m always learning from conversations.',
    'what do you do for fun?': 'I chat with people like you, and that’s always fun!',
    'can you tell me a riddle?': 'Sure! What has keys but can’t open locks? A piano!',
    'how do you work?': 'I work by processing your input and giving you the best response I know!',
    'who made you?': 'I was created by Durgesh, a talented programmer!',
    'do you believe in aliens?': 'I haven’t met any aliens, but I think the universe is vast enough to have many mysteries!'
}

def get_response(query):
    return responses.get(query.lower(), "I don't understand that.")

main = Tk()

main.geometry("400x550")
main.title("My Chatbot")

img_path = "bot3.png"
img = Image.open(img_path)
img = img.resize((161, 165), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

photoL = Label(main, image=img)
photoL.pack(pady=5)

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Your bot is listening, try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("Not recognized")

def ask_from_bot():
    query = textF.get()
    answer_from_bot = get_response(query)
    msgs.insert(END, "You: " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "Bot: " + answer_from_bot)
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target=repeatL)
t.start()

main.mainloop()
