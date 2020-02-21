m,n=map(int,input().split())
a=list(map(int,input().strip().split()))[:m]
if n in a: 
    print(a.index(n))
elif n not in a:
    ans=[]
    for i in range(0,m):
        if a[i] < n:
            ans.append(a.index(a[i]))
    print(max(ans))
else:
    print(-1)