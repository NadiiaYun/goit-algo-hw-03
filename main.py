# Homework 3.1
print('Завдання 1')
# Імпорт модулю datetime
import datetime 

from datetime import datetime

def get_days_from_today(date)-> int:  

    # Перетворення рядка в об'єкт datetime
    target_date = datetime.strptime(date, "%Y-%m-%d").date()
    print('Задана дата: ', target_date)

    # Отримання поточної дати
    current_date = datetime.today().date()
    print('Поточна дата:', current_date)

    # Розрахунок різниці між поточною датою та заданою датою
    diff_days = current_date - target_date 
    #print(diff_days)

    return diff_days.days

#date_string = "2024-10-09"
sign = True
while sign:
    date_string = str(input("Задайте дату: "))   

    try:      
        datetime.strptime(date_string, "%Y-%m-%d")        

    except ValueError:  
        sign = False  
        print(f"Дата {date_string} не відповідає формату 'YYYY-MM-DD'")

    if sign:
        print('Різниця між поточною датою та заданою датою: ', get_days_from_today(date_string), ' днів')
        sign = False
    else:
        sign = True

# Homework 3.2
# Імпорт модулю random
print('Завдання 2')
import random 

def get_numbers_ticket(min, max, quantity):  
    numbers = []
    # Перевірка вхідних параметрів
    if min >=1:
        if max <=1000:
            for i in range(0, quantity):  
                # генерація випадкового числа
                number = random.randint(min, max)
                while numbers.count(number) != 0: 
                    # print(numbers.count(number))                   
                    number = random.randint(min, max)                    
                numbers += [number]
            numbers.sort()
    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("get_numbers_ticket(1, 49, 6)")
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("get_numbers_ticket(1, 36, 5)")
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(0, 1001, 6)
print("get_numbers_ticket(0, 1001, 6)")
print("Ваші лотерейні числа:", lottery_numbers)