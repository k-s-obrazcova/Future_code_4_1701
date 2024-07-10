import datetime

def add_event(filename, event):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(str(datetime.datetime.now()) + " " + event + "\n")

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



menu()