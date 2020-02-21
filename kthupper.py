n,m=map(str,input().split())
s=list(n)
k=int(m)-1
a=[]
for i in range(0,len(s)):
    if i%k==0 and i!=0:
        c=s[i].upper()
        a.append(c)
        k=k+k
    else:
        c=s[i]
        a.append(c)
a = map(str,a)
print(''.join(a))