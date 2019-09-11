import math

n = int(input())

for i in range(n):
    term = int(input())
    row = float((-1 + (1 + (8 * term)) ** 0.5)/2)
    row2 = int(math.ceil(row))

    pos = term - (row2 * (row2 -1)) / 2

    a = row2 - pos + 1

    if row2 % 2 == 0:
        print(f'TERM {term} IS {int(pos)}/{int(a)}')
    else:
        print(f'TERM {term} IS {int(a)}/{int(pos)}')