import json
import os

def create_user(name, role):
    return {"name": name, "role": role, "grades": []}
def load_data(filename='school.json'):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return []

def save_data(users, filename='school.json'):
    with open(filename, 'w') as file:
        json.dump(users, file)

def menu():
    users = load_data()
    while True:
        print("1. Создать пользователя: ")
        print("2. Добавить оценку студенту: ")
        print("3. Посмотреть данные студента: ")
        print("4. Посмотреть данные преподавателя: ")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            name = input("Введите имя пользователя")
            role = input("Введите роль (student / teacher)")
            users.append(create_user(name, role))
            save_data(users)


menu()