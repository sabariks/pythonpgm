import math 
n=int(input())
l=[]
for i in range(0,n+1):
    if i%2!=0:
        l.append(math.factorial(i))
print(*l)