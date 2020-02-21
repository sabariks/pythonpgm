
m,n=map(int,input().split())
list_1=list(map(int,input().strip().split()))[:m]
list_1 = (list_1[-n:] + list_1[:-n]) 
print(*list_1) 