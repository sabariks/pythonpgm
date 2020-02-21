m=int(input())
a=list(map(str,input().strip().split()))[:m]
b=list(set(a))
print(*b)