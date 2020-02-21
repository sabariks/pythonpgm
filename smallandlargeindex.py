m=int(input())
a=[]
a=list(map(str,input().index().strip().split()))[:m]
print(a.index(min(a)),a.index(max(a)))