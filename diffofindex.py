n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=a.index(min(a))
c=a.index(max(a))
print(c-b)