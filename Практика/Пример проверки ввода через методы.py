#блок определения функций
def input_num(string):
    while True:
        x = input(string)
        if x.isdigit():
            return int(x)
        else:
            print('Вы ввели не число. Попробуйте ещё.')

def input_alpha(string):
    while True:
        x = input(string)
        if x.isalpha():
            return x
        else:
            print('Вы ввели строку состоящую не только из алфавитных сиволов')
            
age = input_num('Введите свой возраст (в годах) > ')
rost = input_num('Введите свой рост (в см) > ')
name = input_alpha('Введите ваше имя > ')

print('Вас зовут %s, вам %s лет, и ваш рост %S см'%(name, age, rost))


string = 'строка ТексТа, Не ОченЬ БольШАЯ'
print('В верхнем регистре >', string.upper())
print('В нижнем регистре >', string.lower())
print('С заглавной буквы >', string.capitalize())

x = input('Введите число >')
if x.isdigit():#Проверяет введено ли значение только цифровыми символами
    print('Вы ввели число > ', x)
elif x.isalpha():#Проверяет введено ли значение только алфавитными символами
    print('Вы ввели алфавитные символы > ', x)
#Проверяет введено ли значение только цифровыми или алфавитными символами
elif x.isalnum():
    print('Вы ввели цифры и алфавитные символы > ', x)
else:
    print('Вы ввели непонятно что.')
