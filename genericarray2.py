n=int(input())
a=list(map(int,input().strip().split()))[:n]
m=int(input())
count = 0
for i in range (0,n):
    if m==a[i]:
        count +=1
print(count)
