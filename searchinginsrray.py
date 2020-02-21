m,n=map(int,input().split())
a=list(map(int,input().strip().split()))[:m]
if n in a:
    print('yes')
else:
    print('no')