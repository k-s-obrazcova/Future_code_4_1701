import csv
import datetime


def add_animal(name, species, date, weight, enclosure_size):
    with open('zoo.csv', 'a', newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([name, species, date, weight, enclosure_size])


#
# [
#     'Название',
#     'Тигр',
#     'Черепаха',
#     'Слон'
# ]
#
# [
# 'Название',
# 'Тигр',
# 'Черепаха',
# ]

def remove_animal(name):
    lines = list()
    with open('zoo.csv', 'r', newline='') as file:
        reader = csv.reader(file, lineterminator='\n')
        lines.append(next(reader))
        for row in reader:
            if row[0] != name:
                lines.append(row)

    with open('zoo.csv', 'w', newline='') as fileWrite:
        writer = csv.writer(fileWrite, lineterminator='\n')
        writer.writerows(lines)


def view_all_animals():
    with open('zoo.csv', 'r', newline='') as file:
        reader = csv.reader(file, lineterminator='\n')
        next(reader)
        for row in reader:
            print(', '.join(row))


def find_animal_by_species(species):
    with open('zoo.csv', 'r', newline='') as file:
        reader = csv.reader(file, lineterminator='\n')
        next(reader)
        for row in reader:
            if row[1] == species:
                print(', '.join(row))


def update_animal_info(name):
    lines = list()
    with open('zoo.csv', 'r', newline='') as file:
        reader = csv.reader(file, lineterminator='\n')
        lines.append(next(reader))
        for row in reader:
            if row[0] == name:
                print("Текущая информация: ", ', '.join(row))
                print("Введите новую информацию или оставьте пустую строку для сохранения предыдущего значения! ")
                name = input("Введите название животного: ") or row[0]
                species = input("Введите вид животного: ") or row[1]
                date = input("Введите дату рождения животного: ") or row[2]
                weight = input("Введите вес животного: ") or row[3]
                enclosure_size = input("Введите размер вольера: ") or row[4]
                lines.append([name, species, date, weight, enclosure_size])
            else:
                lines.append(row)
    with open('zoo.csv', 'w', newline='') as fileWrite:
        writer = csv.writer(fileWrite, lineterminator='\n')
        writer.writerows(lines)



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
            remove_animal(name)

        elif choice == '3':
            view_all_animals()

        elif choice == '4':
            species = input("Введите вид животного: ")
            find_animal_by_species(species)

        elif choice == '5':
            name = input("Введите название животного: ")
            update_animal_info(name)

        elif choice == '6':
            name = input("Введите имя посещенного животного: ")
            time = datetime.datetime.now()


menu()
