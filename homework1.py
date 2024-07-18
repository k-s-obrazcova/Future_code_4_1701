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
