import math
m,n=map(int,input().split())
res=math.factorial(m)//math.factorial(m-n)
print(res)