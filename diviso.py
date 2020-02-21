m,n=map(int,input().split())
b=1
for i in range(0,n):
    if i*n==m:
        print(i)
    else:
        b=0
if b==0:
    print(max(m,n))