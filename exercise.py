# 1
# import glob
# import os.path
#
# files = glob.glob('./*.py')
# for file in files:
#     print(file)
#     file_size = os.path.getsize(file)
#     print(f"Размер файла {file} - {file_size} байт")

# 2
import csv
import glob
import datetime
import statistics
import timeit


def work_files():
    data = {}
    for filename in glob.glob('*.csv'):
        try:
            date = datetime.datetime.strptime(filename, '%Y-%m-%d.csv').date()
        except ValueError:
            print(f"Файл {filename} был пропущен так как не соответствует формату")
            continue
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            times, temps, humids = zip(
                *[(datetime.datetime.strptime(row[0], '%H:%M:%S').time(),
                   float(row[1]),
                   float(row[2])) for row in reader])
            data[date] = {'times': times, 'temps': temps, 'humids': humids}
    return data

def analyze_data(data):
    for date, values in data.items():
        print(f"Дата: {date}")
        print(f"Среднее значение температуры: {statistics.mean(values['temps'])}")
        print(f"Максимальная температура: {max(values['temps'])}")
        print(f"Минимальная температура: {min(values['temps'])}")




data = work_files()
analyze_data(data)