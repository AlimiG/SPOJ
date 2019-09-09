import math


n = int(input())
total = 0
half_total = 0
quarter_total = 0
three_total = 0
ans = 0
for time in range(n):
    portion = input()
    if portion == '3/4':
        three_total += 1
    elif portion == '1/2':
        half_total += 1
    elif portion == '1/4':
        quarter_total +=1
    else:
        continue

if three_total>=quarter_total:
    ans=math.ceil(three_total+half_total/2.0)

elif three_total< quarter_total:
    quarter_total=quarter_total-three_total
    if half_total%2==0:
        ans = math.ceil(three_total + half_total/2.0 + quarter_total/4.0)
           
    else:
        quarter_total = quarter_total-2
        ans= math.ceil(three_total + half_total/2.0 + quarter_total/4.0)

print(int(ans+1))      





    
    
