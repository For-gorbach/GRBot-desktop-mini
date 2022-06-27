# -------=импорт нужных библиотек и файлов=-------
from pyrogram import Client, filters  # библиотека для работы с юзерботом
from time import sleep  # библиотека для создания задержки
import eel  # библиотека для создания веб интерфейса
from random import randint  # импорт функции генерирования рандомного числа

@eel.expose  # подключаем функцию к модулю eel
def text(text, chats, api_id, api_hash, time):  # функция
    groups_id = eval("("+chats+")")  # превращаем переданную информацию в список а при помощи eval ``убираем`` ковычки превращая текст в список

    print(f"Кол-во групп - {len(groups_id)}")  # пишем кол-во групп

    app = Client("my_account", api_id=api_id, api_hash=api_hash)  # записываем в переменную app то что юзербот будет выполнять все действия от имени юзера, а так же передаем api_id и api_hash которые мы объявили в файле settings.py

    with app:  # начинаем работу с юзером
        while True:
            for id in groups_id:  # проходим по списку id групп
                try:  # отлавливание ошибок
                    print(id)  # пишем id
                    app.send_message(int(id), text)  # отправляем сообщение
                except Exception as ex:  # обрабатываем ошибку
                    print(f"Упс, ТУТ ошибка {ex}")  # пишем ошибку

            print(f"\nЗасыпание на {int(time)} секунд!\n")  # пишем на сколько сек засыпать программе
            sleep(int(time))  # засыпание программы

eel.init("web")  # инициализируем проект в папке web
eel.start("index.html", size=(1000, 800), port=randint(0, 9999))  # запускаем index.html в окне с размером 1000 на 800
