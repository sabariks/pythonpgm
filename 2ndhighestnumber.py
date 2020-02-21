n=int(input())
if 3 <= n <= 106:
    a=list(map(int,input().strip().split()))[:n]
    x=a.index(max(a))
    print(x)
else:
    print('0')