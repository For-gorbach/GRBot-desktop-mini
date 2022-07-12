# -------=импорт нужных библиотек и файлов=-------
from pyrogram import *  # импорт всего из библиотеки для работы с юзерботом
from time import sleep  # библиотека для создания задержки
import eel  # библиотека для создания веб интерфейса
from random import randint  # импорт функции генерирования рандомного числа

@eel.expose  # подключаем функцию к модулю eel
def text(text, chats, api_id, api_hash, time):  # функция
    groups_id = eval("["+chats+"]")  # превращаем переданную информацию в список а при помощи eval ``убираем`` ковычки превращая текст в список

    def join_in_chat(id):  # функция для входа в чат
        try:  # проверка на наличие ошибок
            app.join_chat(app.get_chat(id)["invite_link"])  # входим в чат по ссылке полученной с помощью id
            print(f"Вы вошли в чат с id {id} ({app.get_chat(id)['title']})")  # пишет в какой чат мы зашли
        except errors.exceptions.flood_420.FloodWait:  # если произошла ошибка от того что вы есть в чате то
            pass  # null функция, что бы ничего не происходило

    app = Client("my_account", api_id=api_id, api_hash=api_hash)  # записываем в переменную app то что юзербот будет выполнять все действия от имени юзера, а так же передаем api_id и api_hash которые мы объявили в файле settings.py

    with app:  # начинаем работу с юзером
        while True:
            for id in groups_id:  # проходим по списку id групп
                join_in_chat(int(id))  # запуск функции для входа в чат
                try:  # отлавливание ошибок
                    print(f"Сообщение отправлено в чат {id} ({app.get_chat(id)['title']})")  # пишем в какой чат мы зашли
                    app.send_message(int(id), text)  # отправляем сообщение
                except Exception as ex:  # обрабатываем ошибку
                    print(f"Упс, ТУТ ошибка {ex}")  # пишем ошибку

            print(f"\nЗасыпание на {int(time)} секунд!\n")  # пишем на сколько сек засыпать программе
            sleep(int(time))  # засыпание программы

eel.init("web")  # инициализируем проект в папке web
eel.start("index.html", size=(1280, 800), port=randint(0, 9999))  # запускаем index.html в окне с размером 1000 на 800
