#Подключение модуля для рассчёта сегодняшней даты
from datetime import datetime

def vozrast():
    birth_date_str = input("Введите дату рождения в формате (дд/мм/гггг) через /: \n ")
    try:
        birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - birth_date.year
#Учет дней и месяцев при подсчете возраста
        if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
#Проверка на то, родился ли человек, т.е. проверка на отрицательный возраст
        if age<0:
             print("Вы еще не родились")
#Если все хорошо, то выводит возраст человека
        else:
            print(f"Ваш возраст: {age} лет")
#Ошибка при неправильном вводе данных
    except ValueError:
         print("Ошибка введения даты. Возможно использован неверный формат ввода данных.")

vozrast()
