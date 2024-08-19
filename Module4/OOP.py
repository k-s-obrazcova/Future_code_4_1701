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

def digit_sum(*args):
    result = 0
    for num in args:
        if isinstance(num, (int, float)):
            result += num
    return result


print(digit_sum(1, 2))
print(digit_sum(3, 4, 5))
print(digit_sum(1.5, 2.5, 3.5))
print(digit_sum(1, "2", 3.5))
