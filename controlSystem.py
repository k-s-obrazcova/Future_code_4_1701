import json


def load_data():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": []}


def save_data(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)


def register(username, password, role, users):
    for user in users["users"]:
        if user["username"] == username:
            print("Пользователь с таким ником уже существует!")
            return

    new_user = {
        "username": username,
        "password": password,
        "role": role
    }

    users["users"].append(new_user)
    save_data(users)
    print("Пользователь успешно создан")


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
        if choice == "1":
            username = input("Введите никнейм пользователя: ")
            password = input("Введите пароль пользователя:")
            role = input("Введите роль(1.Admin; 2.User)")
            register(username=username, password=password, role=role, users=data)

menu()