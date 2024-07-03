import datetime
from pytz import timezone

def convert_timezone(zone):
    zone = timezone(zone)
    time = datetime.datetime.now()
    time_in_to_timezone = time.astimezone(zone)
    return time_in_to_timezone


print("""
_________________________________________________
Конвертер времени
_________________________________________________
""")
zone = input("Введите целевой часовой пояс: ")
result = convert_timezone(zone)
print(f"Время в целевом часовом поясе {result}")