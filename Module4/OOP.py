# args = переменное количество аргументов
# def sum_all(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
#
# result = sum_all(1, 2, 3, 4)
# print(result)
# result = sum_all(180, 2)
# print(result)

# Задача 1
# Создайте функцию по сложению 2-х цифр. Используйте проверку для
# входных значений, чтобы складывать только цифры (int или float). Если в
# функцию добавлено больше 2-х цифр, то они также должны быть
# просуммированы и возвращены в качестве результата.

# def digit_sum(*args):
#     result = 0
#     for num in args:
#         if isinstance(num, (int, float)):
#             result += num
#     return result
#
#
# print(digit_sum(1, 2))
# print(digit_sum(3, 4, 5))
# print(digit_sum(1.5, 2.5, 3.5))
# print(digit_sum(1, "2", 3.5))


# ООП
# class Person:
#     def __init__(self, name, age, birthday, number, seria):
#         self.name = name
#         self.age = age
#         self.birthday = birthday
#         self.number_passport = number
#         self.seria_passport = seria
#
#     def speak(self):
#         return (f"Мое имя {self.name}, день рождения {self.birthday}."
#                 f" Мне {self.age}. Паспортные данные {self.seria_passport} {self.number_passport}")
#
#
# person_first = Person("Ксения", 26, "30.05.1997", 474145, 8456)
# person_second = Person("Олег", 21, "15.09.2002", 789781, 1256)
# print(person_first.speak())
# print(person_second.speak())
# print(person_first.age)
# print(person_first.name)


# Наследование
#Родительский класс
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         return (f"Мое имя {self.name}, день рождения. Мне {self.age}.")

#Дочерний класс
# class Employee(Person):
#     def __init__(self, name, age, rang):
#         super().__init__(name, age)
#         self.rang = rang
#
#     def speak(self):
#         return (f"Мое имя {self.name}, день рождения. Мне {self.age}. Моя должность {self.rang}")
#
#
# person = Person("Алиса", 30)
# employee = Employee("Кирилл", 28, "Юрист")
#
# print(person.speak())
# print(employee.speak())


#Инкапсуляция
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def speak(self):
        return (f"Мое имя {self.get_name()}, день рождения. Мне {self.get_age()}.")

person = Person("Ольга", 50)
print(person.get_name())
print(person.speak())