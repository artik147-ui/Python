# Блок загрузки модулей
import random
#
def vvod_chisla(string):
    while True:
        vvod = input(string).strip()
        if vvod.isdigit():
            return int(vvod)
        else:
            print('Вы ввели не число. Попробуйте ещё раз')

print('''
                Программа угадай число
Сначала Вы должны определить диапазон чисел в котором
будет загадано число
Затем компьютер загадав число попросит Вас ввести Ваш вариант
Если ваше число больше загадонного, то компьютер скажет Больше,
Если ваше число меньше загадонного, то компьютер скажет Меньше
''')
while True: # Цикл отвечает за ввод игроком правильных чисел
    nach = vvod_chisla('Введиите начало диапазона > ')
    konec = vvod_chisla('Введиите конец диапазона > ')
    if nach == konec:
        print('''
    Начало диапазона равно его концу,
    Игра не имеет смысла
    ''')
    elif nach > konec and abs(konec - nach) > 5:
        print('''
    Начало диапазона больше его конца,
    Меняем их местами
    ''')
        nach, konec = konec, nach
        break
    elif (konec - nach) < 5:
        print('''
    Диапазон меньше 5, игра не имеет смысла
    ''')
    
    else:
        break

rand_num = random.randint(nach, konec) # Выбираем случайное число

#print(nach, konec, rand_num) # отладочный блок

while True:
     vvod = vvod_chisla('Введиите ваш вариант числа > ')
     if vvod < nach or vvod > konec:
         print("Будьте внимательны! Ваше число не соответствует диапазону")
     elif vvod < rand_num:
         print('Ваше число меньше загадоного')
     elif vvod > rand_num:
         print('Ваше число больше загадоного')
     else:
         print('Вы угадали!')
         break
