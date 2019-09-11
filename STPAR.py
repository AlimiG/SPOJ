def checkout(size,cars):
    need = 1
    status = True
    street = []

    for car in cars:
        while(bool(len(street)) and street[-1] == need):
            need +=1
            street.pop()

        if car == need:
            need +=1
        elif bool(len(street)) and car > street[-1]:
            status = False
            return status
        else:
            street.append(car)
    return status

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        cars = list(map(int,input().split(' ')))
        if checkout(n,cars):
            print('yes')
        else:
            print('no')

main()