m=int(input())
a=list(map(int,input().strip().split()))[:m]
b=[]
for i in range(m):
    b.append(a[i])
a.sort()
if a==b:
    print('yes')
else:
    print('no')
