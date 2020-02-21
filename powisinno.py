m,n=map(int,input().split())
b=0
for i in range(m):
    if pow(n,i)==m:
        b=1
if b==0:
    print('no')
else:
    print('yes')