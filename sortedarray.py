m,n=map(int,input().split())
a=list(map(int,input().strip().split()))[:m]
b=[]
for i in range(m):
    if a[i] < n:
        b.append(a[i])
b.sort()
if len(b) != 0:
    print(*b)
else:
    print(-1)