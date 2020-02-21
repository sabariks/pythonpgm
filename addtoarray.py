m,n=map(int,input().split())
a=list(map(int,input().strip().split()))[:m]
b=list(map(int,input().strip().split()))[:n]
a.sort()
b.sort()
c=b[::-1]
for i in range(0,n):
    a.append(c[i])
print(*a)
