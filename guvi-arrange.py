n=int(input())
a = list(map(int,input().strip().split()))[:n]
l=[]
for i in range(0,len(a)):
    if len(a)!=0:
        b=max(a)
        l.append(b)
        a.remove(b)
    if len(a)!=0:
        c=min(a)
        l.append(c)
        a.remove(c)
l = map(str,l)
print(' '.join(l))

