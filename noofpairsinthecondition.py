n=int(input())
a=list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,n-2):
    j=i+1;k=j+1
    if a[i]*a[j]==a[k]:
        c+=1
print(c)

