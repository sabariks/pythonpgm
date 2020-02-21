m=int(input())
a=list(map(int,input().strip().split()))[:m]
sum=0
for i in range(0,m):
    if a[i] < 0:
        sum +=a[i]
print(sum)
        