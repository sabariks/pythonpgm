n=int(input())
lst=list(map(int,input().split()))[:n]
a=[]
b=[]
for i in range(0,n):
    if i%2!=0:
        a.append(lst[i])
    else:
        b.append(lst[i])
b.sort()
a.sort(reverse=True)
val=n//2
c=[]

if n%2==0:
    for i in range(0,val):
        c.append(b[i])
        c.append(a[i])
    print(*c)
else:
    for i in range(0,val+1):
        c.append(b[i])
        c.append(a[i])
    print(*c)


         