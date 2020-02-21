import math
def lcm(a,b):
    val=a*b//math.gcd(a,b)
    return val
n=int(input())
a=list(map(int,input().split()))[:n]
ans=lcm(a[0],a[1])
for i in  range(2,n):
    ans=lcm(ans,a[i])
print(ans)