n=int(input())
a=list(map(int,input().strip().split()))[:n+1]
b=[i[0] for i in sorted(enumerate(a), key=lambda x:x[1])]
b=b[::-1]
print(*b)