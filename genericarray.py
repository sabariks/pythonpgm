n=int(input())
arr=list(map(int,input().strip().split()))[:n]
b=[]
for i in range(1,n+1):
    s=arr[0]**i
    b.append(s)

print(b)