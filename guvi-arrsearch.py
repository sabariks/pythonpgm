m,n=map(int,input().split())
a=list(map(int,input().strip().split()))[:m]
for i in range(m):
    if n in a:
        print('yes')
    break