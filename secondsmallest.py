m=int(input())
a=list(map(int,input().strip().split()))[:m]
b=[]
for i in  range(0,m):
    if a[i]!=0:
        b.append(1)
    else:
        break
if m==len(b):
    print(-1)
else:
    print(*b)
