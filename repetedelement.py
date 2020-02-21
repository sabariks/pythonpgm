m=int(input())
a=list(map(str,input().strip().split()))[:m]
lst1=[]
for i in range(0,m):
    for j in range(i+1,m):
        if a[i]==a[j]:
            lst1.append(a[i])
if a[i] not in lst1:
    print(a[i])

