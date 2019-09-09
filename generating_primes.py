# Peter wants to generate some prime numbers for his cryptosystem. 
# Help him! Your task is to generate all prime numbers between 
# two given numbers!
#Input
#The input begins with the number t of test cases in a single line (t<=10).
# In each of the next t lines there are two numbers m and n 
# (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.
#Output
#For every test case print all prime numbers p such that m <= p <= n,
#  one number per line, test cases separated by an empty line.
import math
def sieveoferathostenes(num,num1):
    prime = [True for i in range(num + 1)]
    p = 2
    while(p  <= math.sqrt(num)):

        if (prime[p] == True):

            for i in range(p * 2,num + 1 ,p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    listy = []
    for p in range(num1,num + 1):
        if prime[p] == True:
            listy.append(p)
    
    return listy



t = int(input())
output = ''
for a in range(t ) :
    if a > 0:
        output += '\n'
    lower,bigger = input().split(' ')

    for j in sieveoferathostenes(int(bigger),int(lower)):
        output += str(j) + ' '
            

print(output[:-1])
        