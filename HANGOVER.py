while True:
    c = float(input())
    if c == 0.0: break
    cards = 1
    overhang = 0
    while(overhang < c):
        overhang += 1 / (cards + 1)
        cards += 1
    print(f'{cards - 1} card(s)')
    