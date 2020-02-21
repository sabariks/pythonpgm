a=input()
b=list(a)
c=[]
if len(b)%2!=0:
    for i in range(0,len(b)):
        if int((len(b)/2))==i:
            c.append('*')
        else:
            c.append(b[i])
else:
    for i in range(0,len(b)):
        d=int((len(b)/2))
        if d==i or d==i+1:
            c.append('*')
        else:
            c.append(b[i])
c = map(str,c)
print(''.join(c))
