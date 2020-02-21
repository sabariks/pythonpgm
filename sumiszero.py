m=int(input())
a=list(map(int,input().split()))[:m]
sum=0
ans=[]
for i in range(m):
    sum=sum+a[i]
    if sum==0:
        ans.append(i+1)
if len(ans)==0:
    print(-1)
else:
    print(max(ans))