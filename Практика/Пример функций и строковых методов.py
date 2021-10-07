def vvod_chisla(string):
    while True:
        vvod = input(string).strip()
        if vvod.isdigit():
            return int(vvod)
        else:
            print('Вы ввели не число. Попробуйте ещё раз')

def vvod_alpha(string):
    while True:
        vvod2 = input(string).strip().capitalize()
        if vvod2.isalpha():
            return vvod2
        else:
            print('Вы ввели не только алфавитные символы.. Попробуйте ещё раз')

# основная программа

name = vvod_alpha('Введите Ваше имя > ')
surname = vvod_alpha('Введите Вашу фамилию > ')
ves = vvod_chisla('Введите Ваш вес (в кг.) > ')
rost = vvod_chisla('Введите Ваш рост (в см.) > ')
vozrast = vvod_chisla('Введите Ваш возраст (в годах) > ')
day = vvod_chisla('Введите число вашего рождения (ДД) > ')
month = vvod_chisla('Введите месяц вашего рождения (ММ) > ')
year = vvod_chisla('Введите год вашего рождения (ГГГГ) > ')

print(name, surname)
print(ves, rost, vozrast)
print('%s.%s.%s' % (day, month, year))