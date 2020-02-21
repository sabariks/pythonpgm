n=int(input())
a=list(map(int,input().strip().split()))[:n]
ans = 0
for i in range(0,n):
    ans |= a[i]
print(ans)
