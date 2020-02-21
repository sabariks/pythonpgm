
def dup(x,m):
    repeated = [] 
    for i in range(m): 
        k = i + 1
        for j in range(k,m): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated
m=int(input())
x=list(map(int,input().strip().split()))[:m]
ans=dup(x,m)
if ans:
    a=map(str,ans)
    print(' '.join(a))
else:
    print(-1)