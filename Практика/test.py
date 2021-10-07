first_color = input()
second_color = input()
red = "красный"
blue = "синий"
yellow = "желтый"


if first_color == red:
    if second_color == blue:
        print('фиолетовый')
    elif second_color == yellow:
        print('оранжевый')
elif first_color == blue and second_color == yellow or second_color == blue and first_color == yellow:
        print('зеленый')
elif first_color == blue and second_color == red:
    print('фиолетовый')
elif first_color == yellow and second_color == red:
    print('оранжевый')
elif first_color == yellow and second_color == blue:
    print('зеленый')
elif second_color == first_color:
        print(first_color)
if (first_color != red or first_color != blue or first_color != yellow) or (second_color != red or second_color != blue or second_color != yellow):
    print('ошибка цвета')








