n,m=map(int,input().split())
a = list(map(int,input().strip().split()))[:n]
l=[]
for i in range(0,len(a)-1):
    if a[i]<a[i+1]:
        b=a[i+1]-a[i]
        if m<b:
            l.append(1)
        else:
            l.append(0)
    else:
        b=a[i+1]-a[i]
        if m<b:
            l.append(1)
        else:
            l.append(0)
if a[0]<a[n-1]:
    c=a[n-1]-a[0]
    if m<c:
        l.append(1)
    else:
        l.append(0)
else:
    c=a[0]-a[n-1]
    if m<c:
        l.append(1)
    else:
        l.append(0)
        
l = map(str,l)
print(' '.join(l))

