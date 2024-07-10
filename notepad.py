import datetime

def add_event(filename, event):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(str(datetime.datetime.now()) + " " + event + "\n")

def modify_event(filename, index, new_event):
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for i, line in enumerate(lines):
            if i == index - 1:
                file.write(str(datetime.datetime.now()) + ' ' + new_event + '\n')
            else:
                file.write(line)

def delete_event(filename, index):
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for i, line in enumerate(lines):
            if i != index - 1:
                file.write(line)

def view_event(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(f"{i + 1}. {line.split(' ', 1)[1]}")

def menu():
    filename = 'notepad.txt'
    while True:
        print("1. Добавить событие")
        print("2. Изменить событие")
        print("3. Удалить событие")
        print("4. Просмотр всех событий")
        print("5. Выход")
        choice = input("Введите желаемое действие: ")
        if choice == '1':
            event = input("Введите событие: ")
            add_event(filename, event)
        elif choice == '2':
            index = int(input("Введите номер строки для изменения: "))
            new_event = input("Введите событие: ")
            modify_event(filename, index, new_event)
        elif choice == '3':
            index = int(input("Введите номер строки для изменения: "))
            delete_event(filename, index)
        elif choice == '4':
            view_event(filename)

menu()