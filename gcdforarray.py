import math
n=int(input())
a=list(map(int,input().strip().split()))[:n]
g=math.gcd(a[0],a[1])
for i in range(2,n):
        g=math.gcd(g,a[i])
if g!=1:
    print(g)
else:
    print(-1)

