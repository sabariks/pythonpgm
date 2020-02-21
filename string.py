import math
def fun(s):
    for i in range (0,s):
        if math.gcd(i,i+1)==1:
            if s== (i+(i+1)):
                return 1
        else:
            return 0
s=int(input())
if fun(s)==1:
    print('Stiff')
else:
    print('Not stiff')