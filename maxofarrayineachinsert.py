m,n=map(int,input().split())
t = input()
a=list(map(int,input().strip().split()))[:m]
b=list(map(int,input().strip().split()))[:n]
c=[]
for i in range(0,n):
    a.append(b[i])
    c.append(max(a))
print(*c)
