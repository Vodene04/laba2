#Подключение модуля для случайной генерации
import random
def rock_scissors_paper():
    choices=['камень', 'ножницы', 'бумага']
    ai_choice=random.choice(choices)
    your_choice=input("Выберите: камень/ножницы/бумага. \nПожалуйста, введите ваш выбор с маленькой буквы \n")
#Проверка на корректность ввода данных
    if your_choice not in choices:
        print("Неверный ввод данных!")
#Данные введены корректно
    else:
        print(f'Ваш выбор - {your_choice}')
        print(f'Ваш оппонент выбрал: {ai_choice}')
#Случай победы
        if (your_choice=="камень" and ai_choice=="ножницы") or \
            (your_choice=="ножницы" and ai_choice=="бумага") or \
                (your_choice=="бумага" and ai_choice=="ножницы"):
            print("Победа!")
#Случай ничьей 
        elif your_choice==ai_choice:
            print("Ничья!")
#Случай поражения
        else: print ("Поражение!")

#Запуск игры
rock_scissors_paper()

