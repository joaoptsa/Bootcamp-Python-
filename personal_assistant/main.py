import pyttsx3
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
from tkinter import *
from PIL import ImageTk, Image
import pygame
import time
import webbrowser
import wikipedia
import requests
import pywhatkit as kit
import bs4
from pytube import YouTube
from geopy.geocoders import Nominatim


#https://newsapi.org/
NEWS_API_KEY=""
#https://openweathermap.org/
WEATHER_API_KEY=""

#color
BG_COLOUR = "#3d6466"
RED="#e7385b"

#Bot name
USERNAME="alegria"
BOTNAME="kiko"

engine = pyttsx3.init()

#global variables
array_news=[]
temp = {}
desc = []


#functions secondary

def enable_f():
    Text_entry.config(state='normal')
    label_inf.config(state='normal')
    microfone.config(state='normal')

def weather_news(string):
    global temp,desc

    try:
        geolocator = Nominatim(user_agent="teste")
        location = geolocator.geocode(f"{string}")
        lat=round(location.latitude,2)
        lon=round(location.longitude,2)
        URL=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&lang=pt&units=metric"
        weather_data= requests.get(URL).json()
        desc=weather_data["weather"]
        temp=weather_data['main']
        return True
    except:
        information.config(text="Neste momento ocorreu algum problema ")
        return False


def open_site(site):
    try:
        webbrowser.open(str(site))
    except:
        information.config(text="NESTE MOMENTO SEM REDE")


def speakgoogle(text,lang):

    try:
        conversation = gTTS(text=text, lang=lang, slow=False)
        conversation.save('speak.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load("speak.mp3")
        pygame.mixer.music.play()

    except:
        information.config(text="NESTE MOMENTO SEM REDE")


def greet_user():

    hour = datetime.now().hour
    if (hour >= 5) and (hour < 12):
        speakgoogle(f"Bom dia {USERNAME}",'pt')
    elif (hour >= 12) and (hour < 19):
        speakgoogle(f"Boa tarde {USERNAME}",'pt')
    elif (hour >= 19):
        speakgoogle(f"Boa noite {USERNAME}",'pt')
    time.sleep(3)
    speakgoogle(f"Eu sou o {BOTNAME}. O que precisas?",'pt')


def disabled_f():
    Text_entry.config(state='disabled')
    label_inf.config(state='disabled')
    microfone.config(state='disabled')


def find_my_ip():
   try:
        ip_address = requests.get('https://api64.ipify.org?format=json').json()
        return ip_address["ip"]
   except:
        return "Não sei. Liga a internet. "


def play_on_youtube(video):
    try:
        kit.playonyt(video)
        return True
    except:
        return False


def search_on_wikipedia(query):
    try:
        wikipedia.set_lang('pt')
        results = wikipedia.summary(query, sentences=2)
        return results
    except:
        return None

def get_random_advice():
    try:
        res = requests.get("https://api.adviceslip.com/advice").json()
        return res['slip']['advice']
    except:
        return None

def search_on_google(query):
    try:
        kit.search(query)
        return True
    except:
        return False


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    try:
        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
        return res["joke"]
    except:
        return None


def get_latest_news(value):
    news_headlines = []
    try:
        res = requests.get(f"https://newsapi.org/v2/top-headlines?country=pt&category={value}&apiKey={NEWS_API_KEY}").json()
        articles=res["articles"]


        for article in articles:
            news_headlines.append((article["title"],article["url"]))

        return news_headlines[:8]
    except:
        return None


def dioguinho_site():

    try:
        url = "https://dioguinho.com/"
        HTML = requests.get(url)
        soup = bs4.BeautifulSoup(HTML.text, 'html.parser')
        resume=soup.find_all("h2",class_="thumb-title")
        array=[]
        for title in resume:
            text=title.getText()
            array.append(text)
        return array[:8]
    except:
        return None



def send_whatsapp_message(number, message):
    try:
        kit.sendwhatmsg_instantly(f"+351{number}", message)
    except:
        return None


def dowload_youtube(link,typ):

   try:
       yt = YouTube(str(link))
       #print(yt)

       if typ=="audio":
           ys = yt.streams.filter(only_audio=True)
           print(ys)
           ys = ys.get_audio_only("mp4")
           print(ys)

       elif typ=="video":
           ys = yt.streams.get_highest_resolution()

       else:
           return  False

       ys.download()
       return True

   except:
       return False

def split_string(var):
    words = " "
    for word in var.split()[1:]:
        words += word
        words += " "
    return words

def return_pressed():
    take_user_input()

#functions mains


def manger_functions(query):

    if query == "text":
        var=Text_entry.get().lower()
    else:
        var=query.lower()

    if 'ip address'== var:

        ip_address = find_my_ip()
        speakgoogle(f'O teu IP Address é {ip_address}.\n ','pt')
        information.config(text=f'O teu IP Address é  {ip_address}')

    elif 'youtube'== var.split()[0]:

        speakgoogle(f'Ok vou abrir ','pt')
        information.config(text=f'Pesquisar no youtube ')

        if play_on_youtube(var.split()[1:])==False:
            speakgoogle('Não tens net meu jovem bonito', 'pt')

    elif 'wikipédia' == var.split()[0]:

        speakgoogle('Vou procurar no Wikipédia ','pt')
        words=split_string(var)
        time.sleep(4)
        information.config(text=f'wikipédia : {words}')
        results=search_on_wikipedia(words)

        if None==results:
            speakgoogle('Erro , tente novamente', 'pt')
            information.config(text=f'Erro , tente novamente')
        else:
            speakgoogle(f'De acordo  Wikipedia, {results}','pt')

    elif "meteorologia"==var.split()[0]:

        speakgoogle('Meteorologia', 'pt')

        try: 
            string=split_string(var)
            weather_news(string)
            time.sleep(3)
            for i in desc:
                for key, value in i.items():
                    if "description" == key:
                        speakgoogle(f'O tempo vai estar {value}  ', 'pt')
                        information.config(text=f'Vai estar {value} ')

            time.sleep(5)
            speakgoogle(f'A temperatura vai ser {temp["feels_like"]} celsius', 'pt')
        except:
            speakgoogle(f'O comando está incorreto, ai ai ai se te pego ', 'pt')




    elif "ensinamento" == var:

        speakgoogle(f"Ensinamento do dia",'pt')
        advice = get_random_advice()
        time.sleep(3)
        if advice == None:
            speakgoogle(f"Fodaxe não me aptece", 'pt')
        else:
            speakgoogle(advice, 'en')
            information.config(text=f'{advice}')

    elif 'google' == var.split()[0]:

        speakgoogle('Vou abrir ', 'pt')
        words =split_string(var)
        information.config(text=f'Google : {words}')

        if search_on_google(words)==False:
            information.config(text=f'Erro , tente novamente')


    elif 'piada' == var:

        joke = get_random_joke()
        time.sleep(3)
        if joke==None:
            speakgoogle("Agora não me apetece, fica para próxima",'pt')
        else:
            speakgoogle(joke, 'en')
            information.config(text=f'{joke}')


# business or entertainment general or  health or science or sports or technology

    elif 'news' == var.split()[0]:
        global array_news

        if len(var.split())>2:
            speakgoogle("Apenas duas strings serão validas,as outras serão rejeitadas",'pt')
            time.sleep(5)

        if get_latest_news(var.split()[1])==[]:
            information.config(text=f'Error ')
            speakgoogle("Erro na rede, tente novamente", 'pt')

        else:
            array_news = get_latest_news(var.split()[1])
            #print(array_news)
            information.config(text="Processar")
            words =""
            i=0
            for word in  array_news:
                speakgoogle(word[0], 'pt')
                words +=f"{i}: {word[0]} \n"
                information.config(text=words)
                time.sleep(8)
                i=i+1



    elif "open" == var.split()[0]:

        if len(var.split()) > 3:
            information.config(text=f'Só três strings , outras serão descartadas ')

        if "site" == var.split()[1]:
            open_site(var.split()[2])
        elif "news" == var.split()[1]:


            if int(var.split()[2])>=0 and int(var.split()[2])<8 and var.split()[2].isdigit()==True:

                if array_news== []:
                    information.config(text=f'Vai ler o manual \n A lista está vazia ')

                index=array_news[int(var.split()[2])]
                open_site(index[1])
            else:

                information.config(text=f'Error 1.\nVai ler o manual ')
        else:

            information.config(text=f'Error 2.\nVai ler o manual ')

    elif "dioguinho" == var:


         words="Dioguinho Fofocas fresquinhas\n"
         array=dioguinho_site()

         if array ==None:

             information.config(text=f'Error ')
             speakgoogle("Erro na rede, tente novamente", 'pt')

         else:
             i=0
             for word in array:
                 speakgoogle(word, 'pt')
                 words += f"{word} \n"
                 information.config(text=words)
                 time.sleep(7)
                 i = i + 1

    

    elif "whatsapp" == var.split()[0]:

        number = var.split()[1]
        text=var.split()[2:]
        message=" "
        for word in text:
            message += f"{word} "

        if send_whatsapp_message(number, message)== True:
            speakgoogle("Enviada.","pt")
        else:
            speakgoogle("Não foi Enviada.","pt")

    elif "dowloadtube" == var.split()[0]:

        link = var.split()[1]
        tp = var.split()[2]


        if dowload_youtube(link,tp) == False:
            speakgoogle("Erro no dowload.",'pt')

        else:
            speakgoogle("Esta feito o dowload.",'pt')


    else :
        speakgoogle(f'Não existe este comando. Vai ler o manual ', 'pt')


#microfone

def take_user_input():
    disabled_f()

    r = sr.Recognizer()



    with sr.Microphone() as source:
            print('Listening....')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            speakgoogle('Fala', 'pt')
            audio = r.listen(source)

    try:
        print('Recognizing...')
        speakgoogle('Processar', 'pt')
        query = r.recognize_google(audio, language='pt-br')
        print(f'{query}')

        if not 'sair' in query or 'stop' in query:

            speakgoogle(query, 'pt')
            enable_f()
            manger_functions(query)

        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speakgoogle("Boa noite", 'pt')
            else:
                speakgoogle('Tem um bom dia ', 'pt')


    except Exception:
        speakgoogle('Não percebi . Pode repetir', 'pt')
        time.sleep(3)
        #enable_f()
        take_user_input()


# interface

if __name__ == '__main__':



    window = Tk()
    window.title("Bot Kiko")
    window.minsize(width=500, height=500)
    window.config(padx=50, pady=50, bg=BG_COLOUR,)

    canvas = Canvas(width=200, height=200)
    pic=Image.open("robot.jpg")
    rezide=pic.resize((300,300),Image.Resampling.LANCZOS)
    new_image=ImageTk.PhotoImage(rezide)
    canvas.create_image(100, 150, image=new_image)
    canvas.place(x=0,y=0)

    microfone = Button(text="Ligar o microfone",command=take_user_input,bg="#28393a",
	fg="white",activebackground="#badee2",
		activeforeground="black",)
    microfone.place(x=30,y=200)

    Text_entry = Entry(width=25)
    Text_entry.insert(0,"Digite os comandos")
    Text_entry.place(x=200,y=350)

    credit = Label(window, text="Created by joni",font=('Helvatical bold',10),fg="#8B008B")
    credit.place(x=300,y=400)

    label_inf= Button(text='Enviar', font='Arial ',command= lambda: manger_functions('text'),bg="#28393a",
		fg="white",activebackground="#badee2",
		activeforeground="black",)
    label_inf.place(x=120, y=390)

    information = Label(text='Bem vindo meu amigo!!\n', font='Calibri 10',highlightthickness=0,fg="#A52A2A",)
    information.place(x=230, y=50)
    greet_user()
    window.bind('<Return>',lambda event:return_pressed())
    window.mainloop()

