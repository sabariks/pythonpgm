a,b=map(int,input().split())
lst=list(map(int,input().split()))[:a]
lst.sort(reverse=False)
sum=0
c=0
for i in range(0,a):
    sum=sum+lst[i]
    if sum<=b:
        c=c+1
print(c)