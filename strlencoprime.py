import math
m,n=map(str,input().split())
a=len(m)
b=len(n)
if math.gcd(a,b)==1:
    print('yes')
else:
    print('no')