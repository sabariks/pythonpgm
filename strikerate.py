n=int(input())
a=list(map(float,input().split()))[:n]
print(a)
for i in range(0,n-1):
    n=round(a[i])
    m=round(a[i+1])
    if m-n==1:
        print(a[i],a[i+1])
        break