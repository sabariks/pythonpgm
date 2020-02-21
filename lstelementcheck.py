n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=list(map(int,input().strip().split()))[:n] 
lst=[] 
ans = []
for i  in range(0,n):
    if a[i] in b:
        lst.append(a[i])
if len(lst) == 0:
    print(-1)
else:
    for i in lst:
        if i not in ans:
            ans.append(i)
    print(*ans)
