m=int(input())
a=list(map(int,input().strip().split()))[:m]
date=int(input())
lst=[]
for i in range(0,m):
    if a[i]%date==0:
        lst.append(1)
    else:
        lst.append(0)
print(*lst)