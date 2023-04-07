def p1():
    color1 = input("Введите первый цвет")
    color2 = input("Введите второй цвет")

    if (color1 == 'красный' or color1 == 'синий' or color1 == 'желтый') and (
            color2 == 'красный' or color2 == 'синий' or color2 == 'желтый'):
        if color1 == 'красный' and color2 == 'синий':
            print('фиолетовый')
        if color1 == 'красный' and color2 == 'желтый':
            print('оранжевый')
        if color1 == 'синий' and color2 == 'желтый':
            print('зеленый')
    else:
        print('Можно вводить только красный, синий или зеленый')
def p2():
    password = input('введите пароль')
    if len(password) < 8:
        print('короткий пароль')
    elif password[0:9] == "xyubassln":
        print('слабый пароль')
    else:
        print('ok')

def p3():
    god = int(input())
    if (god % 4 == 0) and (god % 100 != 0) or (god % 400 == 0):
        print('да')
    else:
        print('нет')

def p4():
    vagon = int(input('номер места в вагоне'))
    print()
    if vagon >= 36:
        print('ваше место боковое')
    elif vagon % 2:
        print('ваше место внизу')
    else:
        print('ваше место наверзу')

p2()