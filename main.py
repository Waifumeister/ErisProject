import speech_recognition as sr
import tkinter as tk
import pyttsx3
import webbrowser
import requests
from tkinter import *
from PIL import ImageTk, Image
from geopy.geocoders import Nominatim

# Инициализация распознавателя речи
r = sr.Recognizer()

# Инициализация синтезатора речи
engine = pyttsx3.init()

# Функция для распознавания речи
def recognize_speech():
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='ru-RU')
        print("Вы сказали", text)
        return text
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи; {0}".format(e))
    return ""

# Функция для синтеза речи
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функция для получения координат города
def get_coordinates(city):
    geolocator = Nominatim(user_agent="Eris")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None

# Функция для получения погоды
def get_weather(latitude, longitude):
    api_key = '6e4ea426d43b67aa3ad2fe049a4ba7b4'
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    speak(f"Температура в данном городе составляет {temperature} градусов по Цельсию.")

# Функция выполнения команд
def execute_command(command):
    if 'привет' in command:
        speak("Привет! Чем могу помочь?")
    elif 'пока' in command:
        speak("До свидания!")
    elif 'погода' in command:
        speak("В каком городе вы хотите узнать погоду?")
        city = recognize_speech()
        if city:
            coordinates = get_coordinates(city)
        else:
            speak("Не удалось определить координаты города. Пожалуйста, попробуйте еще раз.")
        if coordinates:
                latitude, longitude = coordinates
                get_weather(latitude, longitude)
        else:
            speak("Извините, не удалось распознать город. Пожалуйста, попробуйте еще раз.")
    if 'открой ютуб' in command:
        speak("Открываю YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif "спасибо" in command:
        speak("Пожалуйста! Если у вас есть еще вопросы, обращайтесь.")

# Задача для кнопки
def on_button_click():
    command=recognize_speech().lower()
    execute_command(command)


window=Tk()
window.title("Головой помощник Eris")
window.geometry("884x1080")
# Добавление файла картинок
image_0=Image.open("C:\\Users\\79001\\Desktop\\3hFWXR4q6Hw.jpg")
image_1=Image.open("C:\\Users\\79001\\Desktop\\кнопка.png")
butt= ImageTk.PhotoImage(image_1)
bg = ImageTk.PhotoImage(image_0)

label=Label(window, image=bg)
label2=Label(window, text="Привет, это голосовой ассистент Eris! ver 1.0", font=("Times New Roman", 24))
label.place(x=0, y=0)
label2.pack(pady=10)

button=Button(window, image=butt, command=on_button_click)
button.place(x=0, y=0)
button.pack(pady=10)

window.mainloop()