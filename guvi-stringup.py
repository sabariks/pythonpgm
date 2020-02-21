s= input()
a=[]
for i in range(0,len(s)):
    if i%2!=0:
        c=s[i].upper()
        a.append(c)
    else:
        c=s[i]
        a.append(c)
a = map(str,a)
print(''.join(a))