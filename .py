n=int(input())
ls=list(map(str,input().strip().split()))[:n]
ls.sort()
for i in range(0,n-1):
    if len(ls[i]) > len(ls[i+1]):
        ls[i],ls[i+1]=ls[i+1],ls[i]
print(*ls)