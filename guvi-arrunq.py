n=int(input())
a = list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,n-1):
    if a[i] in a:
        c=c+1
        if c >=2:
            print (a[i])
            c=0
        else:
            print('-1')
