m = {}
def coin(n):
    if n == 0: return n 
    if not n in m:
        m[n] = max(n, coin(n//2) + coin(n//3) + coin(n//4))
    return m[n]

for i in range(10):
    print(coin(int(input())))