import random
import datetime

""" Рандомна генерація дат для первірки коду.
# random.seed(123)

# Генерація рандомного року
def rand_year():
    b_year = datetime.datetime(random.randint(1950, 2000), 1, 1).year
    return b_year

# Генерація рандомних днів народження
def rand_bday():

    # Генерація рандомного місяця та дня
    month = random.randint(1, 12)
    if month in [2] and rand_year() % 4 != 0:
        day = random.randint(1, 28)
    elif month in [2] and rand_year() % 4 == 0:
        day = random.randint(1, 29) # Для високосного року
    elif month in [1,3,5,7,8,10,12]:
        day = random.randint(1,31)
    elif month in [4,6,9,11]:
        day = random.randint(1,30)
     
    # Створюємо datetime дату
    date = datetime.datetime(rand_year(), month, day).date()

    return date
 
users = [
    {'name': 'Alice', 'birthday':  rand_bday()},
    {'name': 'Bob', 'birthday':  rand_bday()},
    {'name': 'Charlie', 'birthday':  rand_bday()},
    {'name': 'David', 'birthday':  rand_bday()},
    {'name': 'Eve', 'birthday': rand_bday()}
] # список з псевно-рандомними днями народження"""


# Тестовий список іменнинників

users = [
    {'name': 'Alice', 'birthday': datetime.datetime(1990, 2, 18)},
    {'name': 'Bob', 'birthday': datetime.datetime(1992, 1, 25)},
    {'name': 'Charlie', 'birthday': datetime.datetime(1985, 2, 25)},
    {'name': 'David', 'birthday': datetime.datetime(1988, 3, 2)},
    {'name': 'Eve', 'birthday': datetime.datetime(1983, 3, 2)}
]    

def get_birthdays_per_week(names):
    today = datetime.datetime.today().date()
    b_days = {
        0: [], # Monday
        1: [], # Wednesday
        2: [], # Tuesday 
        3: [], # Thursday 
        4: [], # Friday
        5: [], # Saturday
        6: [], # Sunday
    }
    
    future_bday = [] # для переліку людей у яких буде ДР пізніше ніж наступного тижня
    for user in users:
        username = user['name']
        user_bday = datetime.date(datetime.datetime.today().year, user['birthday'].month, user['birthday'].day)
        days_till_list = []
        
        if today.month == user_bday.month and today.day <= user_bday.day:
            days_till_list.append(user_bday.day - today.day)
        if (user_bday - today).days > 7:
            future_bday.append((username, user_bday))
        # Розшируємо значення в  b_days в залежності від дня тижня на коли припадає ДР
        for days in days_till_list:
            if days>= 0 and days < 7:
                if user_bday.weekday() in [5, 6]:
                    b_days[0].append(f'{username} має ДР  {user_bday:%m.%d}')
                elif user_bday.weekday() not in [5, 6]:
                    b_days[user_bday.weekday()].append(f'{username} має ДР  {user_bday:%m.%d}')
    # ДОДАТКОВО: На випадок якщо ні в кого не буде ДР на тижні 
    if not any(b_days.values()):
        print(f'На майбутній тиждень дня народження ні в кого нема!')
        if future_bday:
            sorted_future_bday = sorted(future_bday, key=lambda x: x[1])
            finalochka = [(a, b) for a, b in sorted_future_bday if b == sorted_future_bday[0][1]]
            names = [n for n, d in finalochka]
            names_str = ', '.join(names)
            print(f'Найближчий ДР {finalochka[0][1]} у: {names_str}')
    # Кінцевий вивід, якщо є люди котрі втрапили у критерії виводу         
    else:
        for wday, val in b_days.items():
            if val:
                day_name = datetime.date(1, 1, wday+1).strftime('%A')
                val_str = [str(x) for x in val] # конвертуємо в стрігну, бо інакше викликає помилку
                print(f'{day_name}: {", ".join(val_str)}')


if __name__ == "__main__":
    get_birthdays_per_week(users)


