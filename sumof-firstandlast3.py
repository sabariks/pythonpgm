m=int(input())
a=list(map(int,input().strip().split()))[:m]
ls1=sum(a[:3])
ls2=sum(a[len(a)-3:])
if ls1==ls2:
    print(1)
else:
    print(0)