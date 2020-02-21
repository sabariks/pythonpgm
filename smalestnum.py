m,n=map(int,input().split())
a=list(map(int,input().split()))[:m]
b=[]
for i in range(m):
    if a[i]==n:
        print(n)
        break
    elif a[i] < n:
        b.append(a[i])
if n not in a:
    print(max(b))
