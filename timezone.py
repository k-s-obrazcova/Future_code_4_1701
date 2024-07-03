import datetime
from pytz import timezone, all_timezones, common_timezones

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
print("Доступные часовые зоны: ")
for tzone in all_timezones:
    print(tzone)
while True:
    zone = input("Введите целевой часовой пояс: ")
    if zone in all_timezones:
        break
    else:
        print("Ввод не корректен, введите еще раз")

result = convert_timezone(zone)
print(f"Время в целевом часовом поясе {result}")