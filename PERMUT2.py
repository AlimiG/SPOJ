def inverserpermutation(arr,size):
    arr2 = [0]*(size)
    for i in range(size):
        arr2[arr[i] - 1] = i +1

    return arr2

while True:
    n = int(input())
    if n == 0: break
    integers = list(map(int,input().split(' ')))
    if integers == inverserpermutation(integers,n):
        print('ambiguous')
    else:
        print('not ambiguous')
        