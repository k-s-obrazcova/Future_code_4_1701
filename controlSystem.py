import json

def load_data():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}

def menu():
    data = load_data()
    user = None
    while True:
        print("1.Регистрация; ")
        print("2.Авторизация; ")
        print("3. Проверить доступ; ")
        print("4. Проверить всех сотрудников; ")
        print("5. Выход; ")

        choice = input("Выберите действие: ")