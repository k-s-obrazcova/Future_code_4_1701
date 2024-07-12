import csv


def add_animal(name, species, date, weight, enclosure_size):
    with open('zoo.csv', 'a', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([name, species, date, weight, enclosure_size])


def remove_animal(name):


def menu():
    while True:
        print("1. Добавить животное")
        print("2. Удалить животное")
        print("3. Посмотреть информацию о всех животных")
        print("4. Найти животное по виду")
        print("5. Обновить информацию о животном")
        print("6. Создать время посещения")
        print("7. Выход")
        choice = input("Введите действие: ")
        if choice == '1':
            name = input("Введите название животного: ")
            species = input("Введите вид животного: ")
            date = input("Введите дату рождения животного: ")
            weight = input("Введите вес животного: ")
            enclosure_size = input("Размер вольера: ")
            add_animal(name=name, species=species, date=date, weight=weight, enclosure_size=enclosure_size)


        elif choice == '2':
            name = input("Введите название животного: ")


menu()