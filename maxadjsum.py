n=int(input())
lst=list(map(int,input().split()))[:n]
b=[]
for i in range(0,n-1):
    b.append(lst[i]+lst[i+1])
print(max(b))