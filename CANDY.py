while True:
    N = int(input())
    if N == -1: break
    array = [int(input()) for j in range(N)]
    s = sum(array)
    if s % N:
        print(-1)
    else:
        t = sum(abs(s/N-a) for a in array) /2
        print(int(t))
