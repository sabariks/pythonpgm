m=int(input())
a=list(map(int,input().strip().split()))[:m]
for i in range(0,m):
    for j in range(i+1,m):
        if a[i]!=a[j]:
            print(a[i])
