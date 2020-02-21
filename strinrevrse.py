l=list(map(str,input().strip().split()))
ans=[]
ans.append(l[0])
for i in range(1,len(l)-1):
    ls=list(l[i])
    ls.reverse()
    s=str(ls)
    ans.append(ls)
a=len(l)
ans.append(a)
print(ans)