a,k=map(str,input().split())
s=list(a)
s.insert(0,0)
ans = []
for i in range(0,len(s)):
    if s[i]==k:
        ans.append(str(i))
        break
if len(ans)>0:
    print(''.join(ans))
else:
    print(-1)
