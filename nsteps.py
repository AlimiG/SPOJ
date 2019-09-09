

times = int(input())
for time in range(times):
    x,y = input().split(' ')
    x = int(x)
    y = int(y)
    if y == x:
        if x % 2 == 0:
            print(2 * x)
        else:
            print((2 * x) -1)
    elif x == y + 2:
        if x % 2 == 0:
            print(x + y)
        else:
            print(x + y -1)
    else:
        print('No Number')

