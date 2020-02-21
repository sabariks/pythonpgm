# def gcd(a,b): 
#     if(b==0): 
#         return a 
#     else: 
#         return gcd(b,a) 
a,b=map(int,input().strip().split())
import math
c=math.factorial(a)
d=math.factorial(b)
if a==0 or b==0:
    print(max(a,b))
else:
    print(math.gcd(c,d))
