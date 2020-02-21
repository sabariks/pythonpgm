a=input()
b=list(a)
c=[]
n=len(b)
for i in range(0,n):
    d=b.count(b[i])
    c.append(b[i])
    c.append(d)
for i in range(0,n):
    if c[i]==c[i+2]:
        c.remove(c[i+1])
        c.remove(c[i+3])
c = map(str,c)
print(''.join(c))

