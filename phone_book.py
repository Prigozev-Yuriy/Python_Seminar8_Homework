# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. + Программа должна выводить данные
# 2. + Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os
import time


def input_name():
    name = input("Введите имя: ")
    return name

def input_surname():
    surname = input("Введите фамилию: ")
    return surname

def input_patronymic():
    patronymic = input("Введите отчество: ")
    return patronymic

def input_phone():
    phone = input("Введите номер телефона: ")
    return phone

def input_address():
    address = input("Введите адрес: ")
    return address

def input_data():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    with open("phone_book.txt", "a",encoding="utf-8") as data:
        data.write(f"{name} {surname} {patronymic}\n{phone}\n{address}\n\n")

def print_data():
    os.system("cls")
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        print(data.read())

def search_line():
    search = input("Введите значение поиска: ")
    with open("phone_book.txt", "r",encoding="utf-8") as data:
        text = data.read().split("\n\n")[:-1]
        
        # data.seek(0)
        # list_data = data.readlines()
        for line in text:
            # print(line)
            # print()
            # time.sleep(1)
            if search in line:
                print(line)
                print()

def interface():
    cmd = ""
    while cmd != "4":
        print("Выберите вариант действия: \n"\
            "1.Записать данные\n"\
            "2.Вывести данные\n"\
            "3.Поиск данных\n"\
            "4.Выход"  )
        cmd = input("Введите номер операции: ")
        while cmd not in ("1", "2", "3", "4"):
            print("Ввод неверный")
            cmd = input("Введите номер операции: ")
        if cmd == "1":
            input_data()
        elif cmd == "2":
            print_data()
        elif cmd == "3":
            search_line()


interface()

    






    