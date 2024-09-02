import random

number_to_guess = random.randint(1, 1000)
guess = None
attempts = 0

print("""
______________________________________________
Добро пожаловать в игру!
______________________________________________
Вам необходимо будет угадать число от 1 до 1000
______________________________________________
""")
while guess != number_to_guess:
    guess = int(input("Введи свое число: "))
    attempts += 1
    if guess < number_to_guess:
        print("Ты был близок, но пока мало")
    elif guess > number_to_guess:
        print("Ты был близок, но слишком много")

print(f"Поздравляю, вы угадали число {number_to_guess}, угадано за {attempts} попыток")
