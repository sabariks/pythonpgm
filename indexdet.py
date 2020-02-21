m=int(input())
a=list(map(int,input().split()))[:m]
b=[]
for i in range(m):
    if i==a[i]:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    print(*b)