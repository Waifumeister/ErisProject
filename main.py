import speech_recognition as sr
import pyttsx3
import webbrowser
from tkinter import *
from pyowm import OWM
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require("1.11.1")

class VoiceAssistantApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10)

        label = Label(text="Привет, это голосовой ассистент Eris! ver 1.0", font_size=24, size_hint=(1, 0.2))
        layout.add_widget(label)

        input_box = TextInput(multiline=False, size_hint=(1, 0.2))
        layout.add_widget(input_box)

        mybutton = Button(
            text='Говорить',
            size=(80, 80),
            size_hint=(None, None)
        )
        mybutton.bind(on_press=self.on_button_click)
        layout.add_widget(mybutton)

        return layout

    # Функция для синтеза речи
    def speak(self, text):
        engine = pyttsx3.init() # Инициализация синтезатора речи
        engine.say(text)
        engine.runAndWait()

    # Функция для распознавания речи
    def recognize_speech(self):
        r = sr.Recognizer() # Инициализация распознавателя речи
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

    # Задача для кнопки
    def on_button_click(self, ss):
        command = self.recognize_speech().lower()
        self.execute_command(command)
# Функция для получения координат города

    def get_weather2(self, city):
        city+=",RU"
        owm = OWM('6e4ea426d43b67aa3ad2fe049a4ba7b4')
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(city)
        w = observation.weather
        return w.temperature('celsius')




# Функция выполнения команд
    def execute_command(self, command, coordinates=None):
        if 'привет' in command:
            self.speak("Привет! Чем могу помочь?")
        elif 'пока' in command:
            self.speak("До свидания!")
        elif 'погода' in command:
            self.speak("В каком городе вы хотите узнать погоду?")
            city = self.recognize_speech()
            coordinates = self.get_weather2(city)
            if city:
                self.speak(f'Погода в городе {city} {coordinates["temp"]} ')
                print(f'Погода в городе {city} {round(coordinates["temp"])} ')
            else:
                self.speak("Не удалось определить координаты города. Пожалуйста, попробуйте еще раз.")

        if 'открой ютуб' in command:
            self.speak("Открываю YouTube")
            webbrowser.open("https://www.youtube.com/")
        elif "спасибо" in command:
            self.speak("Пожалуйста! Если у вас есть еще вопросы, обращайтесь.")


if __name__ == "__main__":
    VoiceAssistantApp().run()



#Задача для кнопки
# def on_button_click():
#     command=recognize_speech().lower()
#     execute_command(command)

#window=Tk()
#window.title("Головой помощник Eris")
#window.geometry("884x1080")
# Добавление файла картинок
#image_0=Image.open("C:\\Users\\79001\\Desktop\\3hFWXR4q6Hw.jpg")
#image_1=Image.open("C:\\Users\\79001\\Desktop\\кнопка.png")
#butt= ImageTk.PhotoImage(image_1)
#bg = ImageTk.PhotoImage(image_0)

#label=Label(window, image=bg)
#label2=Label(window, text="Привет, это голосовой ассистент Eris! ver 1.0", font=("Times New Roman", 24))
#label.place(x=0, y=0)
#label2.pack(pady=10)

#button=Button(window, image=butt, command=on_button_click)
#button.place(x=0, y=0)
#button.pack(pady=10)
#window.mainloop()