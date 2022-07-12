# -------=импорт нужных библиотек и файлов=-------
from pyrogram import *  # импорт всего из библиотеки для работы с юзерботом
from time import sleep  # библиотека для создания задержки
import eel  # библиотека для создания веб интерфейса
from random import randint  # импорт функции генерирования рандомного числа

@eel.expose  # подключаем функцию к модулю eel
def text(text, chats, api_id, api_hash, time):  # функция
    chats = chats.replace("\n", "")  # удаляем все пропуски строк
    chats = chats.replace("\"", "")  # удаляем все ковычки
    chats = chats.replace("'", "")  # удаляем все ковычки
    chats = chats.split(", ")  # разделяем строку по запятым с пробелами
    chats = ",".join(chats)  # соединяем строку запятыми (без пробела)
    groups_links = chats.split(",")  # разделяем строку по запятым (без пробела)

    def join_in_chat(app, link):  # функция для входа в чат
        try:  # проверка на наличие ошибок
            app.join_chat(link)  # входим в чат по ссылке полученной с помощью ссылки
            print(f"Вы вошли в чат {app.get_chat(link).title}")  # пишет в какой чат мы зашли
        except errors.exceptions.flood_420.FloodWait:  # если произошла ошибка от того что вы есть в чате то
            pass  # null функция, что бы ничего не происходило

    app = Client("my_account", api_id=api_id, api_hash=api_hash)  # записываем в переменную app то что юзербот будет выполнять все действия от имени юзера, а так же передаем api_id и api_hash которые мы объявили в файле settings.py

    with app:  # начинаем работу с юзером
        for link in groups_links:  # проходим по списку ссылок групп
            join_in_chat(app, link)  # запуск функции для входа в чат
        while True:
            for link in groups_links:  # проходим по списку ссылок групп
                try:  # отлавливание ошибок
                    print(f"Сообщение отправлено в чат \"{app.get_chat(link).title}\"!")  # пишем в какой чат мы зашли
                    app.send_message(app.get_chat(link).id, text)  # отправляем сообщение
                except Exception as ex:  # обрабатываем ошибку
                    print(f"Упс, ТУТ ошибка {ex}")  # пишем ошибку

            print(f"\nЗасыпание на {int(time)} секунд!\n")  # пишем на сколько сек засыпать программе
            sleep(int(time))  # засыпание программы

eel.init("web")  # инициализируем проект в папке web
try:
    eel.start("index.html", size=(1280, 800), port=randint(0, 9999))  # запускаем index.html в окне с размером 1000 на 800
except FileNotFoundError:
    print("Пожалуйста, проверьте наличие chrome на устройстве!")
    input("Нажмите Enter для закрытия программы!")
exit()  # закрытие консоли при выключении программы
