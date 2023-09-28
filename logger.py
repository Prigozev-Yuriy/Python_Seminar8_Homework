from data_create import*
import os



def create_contact():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    new_contact_str = f"{name} {surname} {patronymic}\n{phone}\n{address}\n\n"
    return new_contact_str


def input_data():
    new_contact = create_contact()
    with open('phone_book.txt', 'a', encoding='utf_8') as data:
        data.write(new_contact + "\n\n")


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


def change_line():
    search = input('Введите имя, фамилию, отчество, номер телефона или адрес: ').title()
    with open('phone_book.txt', 'r', encoding='utf_8') as file:
        list_contacts = file.read().strip().split('\n\n')
        new_list_contacts = []
        for contact_str in list_contacts:
            if search not in contact_str:
                new_list_contacts.append(contact_str)
            else:
                print(f'Контакт найден:\n{contact_str}')
                check = input('Изменить контакт?\n' \
                              '1 - Да\n' \
                              '2 - Нет\n')
                if check == '1':
                    print('Введите новые данные:')
                    new_contact = create_contact()
                    new_list_contacts.append(new_contact)
                else:
                    new_list_contacts.append(contact_str)

    with open('phone_book.txt', 'w', encoding='utf_8') as file:
        new_str_contacts = "\n\n".join(new_list_contacts)
        file.write(new_str_contacts)


def delete_line():
    search = input('Введите имя, фамилию, отчество, номер телефона или адрес: ').title()
    with open('phone_book.txt', 'r', encoding='utf_8') as file:
        list_contacts = file.read().strip().split('\n\n')
        new_list_contacts = []
        for contact_str in list_contacts:
           if search not in contact_str:
                new_list_contacts.append(contact_str)
    with open('phone_book.txt', 'w', encoding='utf_8') as file:
        new_str_contacts = "\n\n".join(new_list_contacts) + "\n\n"
        file.write(new_str_contacts)





            # if search in line:
            #     print(line)
            #     print()

