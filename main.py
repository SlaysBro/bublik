import turtle
from random import randint

colors = []
rand = 1
last_number = 0
rand_colors = ''
rand_colors_repeat = ''
color_count = 1

max_color_count = int(input('Сколько вы хотите цветов у бублика? '))

if max_color_count < 1:
    print('Тогда удали Python!!!')
else:
    if max_color_count > 1:
        rand_colors = input('Вы хотите чтобы цвета сменяли друг друга рандомно? ').lower()
        if rand_colors == 'да' and max_color_count > 2:
            rand_colors_repeat = input('Вы хотите чтобы они шли подряд? ').lower()

    if max_color_count > 1:
        user_color = input(
            'Укажите первый цвет, который вы хотите видеть у бублика (на английском)'
            ' или введите его HEX код (вместе с "#"): ').lower()
    else:
        user_color = input(
            'Укажите цвет, который вы хотите видеть у бублика (на английском)'
            ' или введите его HEX код (вместе с "#"): ').lower()

    colors.append(user_color)   #В конец списка добавляет введённое пользователем значение.
    while color_count < max_color_count:
        color_count += 1
        user_color = input('Укажите {0} цвет: '.format(color_count)).lower()
        colors.append(user_color)   #В конец списка добавляет введённое пользователем значение.

    turtle.speed(20)
    turtle.bgcolor('pink')

    if rand_colors == 'да': 
        for i in range(72):
            rand = randint(0, max_color_count - 1)
            if rand_colors_repeat == 'нет':
                while rand == last_number:  #Цикл который не даёт числам (кругам) повторяться.
                    rand = randint(0, max_color_count - 1)
                last_number = rand  #Присваивает последнему выпавшему числу значение.
            turtle.color(colors[rand])
            turtle.begin_fill()
            turtle.circle(100, 360)
            turtle.end_fill()
            turtle.lt(5)
    else:
        for i in range(72//max_color_count):
            for cr in colors:
                turtle.color(cr)
                turtle.begin_fill()
                turtle.circle(100, 360)
                turtle.end_fill()
                turtle.lt(5)

    turtle.mainloop()
