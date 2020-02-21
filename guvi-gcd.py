def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
a,b=map(int,input().strip().split())
import math
c=math.factorial(a)
d=math.factorial(b)
print(gcd(c,d))
