from datetime import datetime


def days_length(first_date, second_date):
    first_date = datetime.strptime(first_date, "%Y-%m-%d")
    second_date = datetime.strptime(second_date, "%Y-%m-%d")
    return (second_date - first_date).days


first_date = input("¬ведите первую дату в формате YYYY-MM-DD: ")
second_date = input("¬ведите вторую дату в формате YYYY-MM-DD: ")
print(days_length(first_date, second_date))
