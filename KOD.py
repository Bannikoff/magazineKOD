# Тестовое задание на вакансию автора IT-статей

# Хардкодим текущую дату
current_day = 15
current_month = 2
current_year = 2024

# Запрашиваем у пользователя дату рождения
birthdate = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")

# Разделяем дату рождения на день, месяц и год
day, month, year = map(int, birthdate.split('.'))

# Создаем список с количеством дней в каждом месяце, учитывая высокосные года
if current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Считаем количество дней до дня рождения
if month < current_month or (month == current_month and day < current_day):
    # Если день рождения уже прошел в этом году, расчитываем дни до следующего дня рождения
    days_left = sum(days_in_month[current_month-1:]) - current_day + sum(days_in_month[:month-1]) + day
elif month == current_month and day == current_day:
    # Если сегодня день рождения
    days_left = 0
else:
    # Если день рождения еще не наступил в этом году
    days_left = sum(days_in_month[current_month-1:month-1]) - current_day + day
    
# Выводим количество дней до дня рождения
print("До вашего дня рождения осталось", days_left, "дней.")

# Создаем список с знаками зодиака и соответствующими датами
zodiac_signs = [(1, 19, "Козерог"), (2, 18, "Водолей"), (3, 20, "Рыбы"), (4, 19, "Овен"), (5, 20, "Телец"), 
                (6, 20, "Близнецы"), (7, 22, "Рак"), (8, 22, "Лев"), (9, 22, "Дева"), (10, 22, "Весы"), 
                (11, 21, "Скорпион"), (12, 21, "Стрелец"), (1, 31, "Козерог")]

# Определяем знак зодиака
for i in range(len(zodiac_signs)):
    if (month, day) <= (zodiac_signs[i][0], zodiac_signs[i][1]):
        print("По гороскопу вы", zodiac_signs[i][2], ", чтобы это не значило :)")
        break