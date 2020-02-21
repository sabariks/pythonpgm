n=int(input())
a=list(map(int,input().strip().split()))[:n]
k=int(input())
b=[]
for i in range(0,n):
    if a[i]%k !=0:
        b.append(0)
    else:
        b.append(1)
b = map(str,b)
print(' '.join(b))