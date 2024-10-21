#Подключения модуля для генератора чисел
import random

#Функция для генерации случайных чисел
def my_generate(count=10, start=0, stop=200):
    for _ in range(count):
        yield random.randint(start, stop)

def find_multiples():
    X = input("Введите цифру с клавиатуры: ")
    try:
#Проверка на правильность ввода числа X (цифры с клавиатуры)
        X = int(X)
        if 1 <= X < 10:
            numbers = list(my_generate(10, 0, 200)) 
            print(f"Сгенерированные числа: {numbers}")
#Использование лямбда-функции
            multiples = list(filter(lambda num: num % X == 0, numbers))
            if multiples:
                print(f"Числа, кратные {X}: {multiples}")
            else:
                print(f"Нет чисел, кратных {X}.")
#Если введен 0, который считается цифрой с клавиатуры, то программа выдаст характерное сообщение:
        elif X==0:
            print("На ноль делить нельзя.")
#Если введено целое число больше 9 или меньше 0, то выведет ошибку
        else:
            print("Ошибка ввода. Введите цифру.")
#Если введено не число, то выведет ошибку
    except ValueError:
        print("Ошибка ввода. Введите цифру.")

find_multiples()
