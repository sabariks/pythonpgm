a = list(map(str,input().strip().split()))
b=[]
for i in range(0,len(a)):
    if i%2==0:
        str=a[i]
        c=str.upper()
        b.append(c)
    else:
        str=a[i]
        c=str.lower()
        b.append(c)
print(' '.join(b))