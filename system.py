import glob
import pandas
import statistics
import timeit


def calculate_time_and_weight(directory, column):
    start_time = timeit.default_timer()
    file = glob.glob(directory + "/zoo.csv")
    if file:
        data = pandas.read_csv(file[0], encoding='windows-1251')
        if column in data.columns:
            data[column] = data[column].str.replace(',', '.').astype(float)
            mean = statistics.mean(data[column])
        else:
            return f"Столбик {column} не найден"
    else:
        return f"Файл zoo.csv не найден в директории {directory}"
    end_time = timeit.default_timer()
    work_time = end_time - start_time
    return mean, work_time


directory = "."
column = "Вес"
mean, work_time = calculate_time_and_weight(directory, column)
print(f"Среднее значение для столбика {column} в файле zoo.csv: {mean}")
print(f"Среднее время работы функции {work_time} секунд")
