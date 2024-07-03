import datetime
calendar = {}
def add_event(date, time, description):
    try:
        date_str = date + " " + time
        datetime_obj = datetime.datetime.strptime(date_str, '%d-%m-%Y %H:%M')
        calendar[datetime_obj] = description

    except ValueError:
        print("Не верный формат даты и времени")


def view_events():
    for event in sorted(calendar.keys()):
        print(f"Дата и время: {event.strftime('%A %d/%m/%Y %H:%M')}, Описание: {calendar[event]}")


def delete_event(date, time):
    try:
        date_str = date + " " + time
        datetime_obj = datetime.datetime.strftime(date_str, '%d-%m-%Y %H:%M')
        if datetime_obj in calendar:
            del calendar[datetime_obj]
        else:
            print("Событие не найдено")

    except ValueError:
        print("Не верный формат даты и времени")

while True:
    print("""
    1. Добавить событие
    2. Посмотреть события
    3. Удалить событие
    4. Выход
    """)
    choice = input("Выберите действие: ")
    if choice == '1':
        date = input("Введите дату: (дд-мм-гггг)")
        time = input("Введите время: (чч:мм)")
        description = input("Введите описание события:")
        add_event(description=description, time=time, date=date)
    elif choice == '2':

    elif choice == '3':

    elif choice == '4':
        print("Спасибо что пользовались нашей программой, до свидания ! :)")
        break
    else:
        print("Неверный выбор, попробуйте еще раз")