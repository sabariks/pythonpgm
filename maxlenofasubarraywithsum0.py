n=int(input())
lst=list(map(int,input().split()))[:n]
a=[]
b=[]
for i in range(0,n):
    a.append(lst[i])
    s=sum(a)
    if s==0:
        b.append(len(a))
if len(b)==0:
    print(-1)
else:
    print(max(b))