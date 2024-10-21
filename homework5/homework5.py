#Функция генератора чисел в диапазоне 30
def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

generation=get_number()

#Поиск первого, пятого и последнего чисел
for index, number in enumerate(generation, start=1):
    if index==1:
        first_numer=number
    if index==5:
        fifth_numer=number
    last_numer=number

#Вывод найденных чисел
print(f"Первое нечётное число: {first_numer}")
print(f"Пятое нечётное число: {fifth_numer}")
print(f"Последнее нечётное число: {last_numer}")
