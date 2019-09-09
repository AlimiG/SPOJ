N = int(input())
for n in range(N):
    a,b = input().split()
    print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))