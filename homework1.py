# -*- coding: utf-8 -*-


# 1

# from datetime import datetime
#
#
# def days_length(first_date, second_date):
#     first_date = datetime.strptime(first_date, "%Y-%m-%d")
#     second_date = datetime.strptime(second_date, "%Y-%m-%d")
#     return (second_date - first_date).days
#
#
# first_date = input("Введите первую дату в формате YYYY-MM-DD: ")
# second_date = input("Введите вторую дату в формате YYYY-MM-DD: ")
# print(days_length(first_date, second_date))

# 2.	Дано текущее время в Москве.
# Необходимо определить, какое сейчас время в Шанхае.

# from datetime import datetime
# import pytz
#
#
# def current_time_in_shanghai():
#     moscow_timezone = pytz.timezone('Europe/Moscow')
#     shanghai_timezone = pytz.timezone('Asia/Shanghai')
#     moscow_time = datetime.now(moscow_timezone)
#     shanghai_time = moscow_time.astimezone(shanghai_timezone)
#     return shanghai_time
#
#
# print(current_time_in_shanghai())


# 3.	На вход подается дата рождения пользователя. Необходимо вычислить его возраст в днях.

# from datetime import datetime
#
#
# def days_birthday(birthday):
#     birthday = datetime.strptime(birthday, "%Y-%m-%d")
#     now = datetime.now()
#     return (now - birthday).days
#
#
# birthday = input("Введите свою дату рождения: ")
# print(days_birthday(birthday))

# 4 На вход подается дата и время начала события и его продолжительность в часах.
# Необходимо определить дату и время окончания события.


# from datetime import datetime, timedelta
#
#
# def event_end(date_start, hours):
#     date_start = datetime.strptime(date_start, "%Y-%m-%d %H:%M:%S")
#     end_time = date_start + timedelta(hours=int(hours))
#     return end_time
#
#
# date_start = input("Введите дату и время в формате YYYY-MM-DD HH:MM:SS ")
# hours = input("Введите продолжительность события в часах: ")
# print(event_end(date_start, hours))


# 5.	Дано время отправления самолета из аэропорта в Москве и время полета до Нью-Йорка.
# Необходимо определить местное время прибытия самолета в Нью-Йорк.
# Учтите, что время полета указано в часах,
# а разница во времени между Москвой и Нью-Йорком составляет -7 часов.

# from datetime import datetime, timedelta
# import pytz
#
#
# def arrival(departure_time, flight_time):
#     moscow_timezone = pytz.timezone('Europe/Moscow')
#     ny_timezone = pytz.timezone('America/New_York')
#     departure_time = datetime.strptime(departure_time, "%Y-%m-%d %H:%M:%S")
#     departure_time = moscow_timezone.localize(departure_time)
#     arrival_time_ny = departure_time + timedelta(hours=int(flight_time))
#     arrival_time_ny = arrival_time_ny.astimezone(ny_timezone)
#     return arrival_time_ny
#
#
# departure = input("Введите время и дату отправки в формате YYYY-MM-DD HH:MM:SS : ")
# flight = input("Введите количество часов в полёте: ")
# print(arrival(departure_time=departure, flight_time=flight))
