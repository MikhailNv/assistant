import speech_recognition as sr
import pyttsx3
import re
from os import system
import webbrowser
#from selenium import webdriver
from fuzzywuzzy.fuzz import ratio as ro

micro = sr.Microphone()
r = sr.Recognizer()
engine = pyttsx3.init()

def talk(x):
    engine.say(x)
    engine.runAndWait()

def listen():
    text = ""
    print("Я вас слушаю:")
    while text == "":
        with micro as source:
            #r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio, language=("RU-ru")).lower()
            except(sr.UnknownValueError, TypeError):
                pass
    print(text)
    return(text)

def cmd(text):
    task = ''
    a = re.split(r' ', text)
    for i in range(len(a)):
        if i == "привет":
            text = i
            break
        elif i == "включи" and i+1 == "музыку":
            text = "включи музыку"
            system(r'C:\Users\Пользователь\Music\"Slava Marlow - Снова Я Напиваюсь.mp3"')
        if i == "пока":
            text = i

    def hi():
        global talk
        talk('приветствую вас! как дела?')

    def bye():
        global talk
        talk('до скорых встреч! не забывайте про меня')
        exit()

    def music():
        global talk
        talk('хорошо! сейчас включу')
        system(r'C:\Users\Пользователь\Music\"Slava Marlow - Снова Я Напиваюсь.mp3"')

    def nice():
        global talk
        talk('замечательно! что для вас сделать?')

    def bad():
        global talk
        talk('оу, это неприятно! но ничего страшного, не расстраивайтесь! предлагаю вам выпить чашечку кофе')

    def vk():
        global talk
        talk('хорошо! общайтесь сколько угодно')
        url = 'https://vk.com/feed'
        webbrowser.open_new_tab(url)
#        driver = webdriver.Chrome()
#        driver.get("https://vk.com/")
#        search = driver.find_element_by_class_name('blind_label')
#        search.click()
    def yt():
        global talk
        talk('хорошо! надеюсь, вы посмотрите что-то хорошее')
        url = 'https://www.youtube.com/'
        webbrowser.open_new_tab(url)

    cmds = {
        ('привет', 'здарова', 'салам', 'хай', 'добрый день', 'приветствую') : hi,
        ('пока', 'уйди', 'замолчи', 'не мешай') : bye,
        ('включи музыку', 'подруби музон') : music,
        ('отлично', 'хорошо', 'нормально', 'более ли менее', 'сойдет', 'средне') : nice,
        ('плохо', 'ужасно', 'отвратительно', 'так себе', 'не очень') : bad,
        ('открой вк', 'запусти вконтакте', 'открой вконтакте') : vk,
        ('открой youtube', 'youtube', 'запусти youtube', 'включи youtube') : yt
    }
    maintask = 0
    k = 0
    for i in cmds:
        for j in i:
            if (ro(j, text) > 70) & (ro(j, text) > k):
                maintask = i
                k = ro(j, text)
    if maintask in cmds:
        cmds[maintask]()
    else:
        pass

while True:
    try:
        cmd(listen())
    except KeyError:
        pass



