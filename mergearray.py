m,n=map(int,input().split())
a=list(map(int,input().strip().split()))[:m]
b=list(map(int,input().strip().split()))[:n]
for i in range(0,n):
    a.append(b[i])
a.sort()
print(*a)
