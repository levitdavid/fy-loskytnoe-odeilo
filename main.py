def printfield(field):  # игровое поле
    """
    Генерирует игровое поле

    """
    for x in field:
        s = ''
        for n in x:
            if n == 0: s += '.'
            if n == 1: s += '1'
            if n == 2: s += '2'
            if n == 3: s += '3'
        print(s)


def straf(field):
    r = [0, 0, 0]
    for igr in (1, 2, 3):
        k = 0
        for stroka in range(4):
            for strofa in range(5):
                if field[stroka][strofa] == igr:
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if di != 0 or dj != 0:
                                i1 = stroka + di
                                j1 = strofa + dj
                                if 0 <= i1 <= 3 and 0 <= j1 <= 4 and field[i1][j1] == igr:
                                    k += 1
        r[igr - 1] = k // 2
    return r


def endgame(field):
    k = 0
    for stroka in range(4):
        for strofa in range(5):
            if field[stroka][strofa] == 0:
                k += 1
    return k == 0


field = [[0] * 5, [0] * 5, [0] * 5, [0] * 5]
igr = 1
while True:
    print('Ход игрока', igr)
    while True:
        try:
            x, y = list(map(int, input('X Y').split()))
        except:
            x, y = 10, 10
        if 1 <= x <= 4 and 1 <= y <= 5 and field[x - 1][y - 1] == 0:
            field[x - 1][y - 1] = igr
            break
        print('Некорректный ход, повторите')
    printfield(field)
    if endgame(field):
        break
    igr += 1
    if igr == 4: igr = 1
r = straf(field)
minr = min(r)
print(r)
winner = [i + 1 for i in range(3) if r[i] == minr]
print('Победил', *winner)