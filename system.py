import glob
import pandas
import statistics
import timeit

def calculate_time_and_weight(directory, column):
    start_time = timeit.default_timer()
    file = glob.glob(directory + "/zoo.csv")
    if file:
        data = pandas.read_csv(file[0])
        if column in data.columns:

        else:
            return f"Столбик с названием {column} не найден"
