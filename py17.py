str=input()
lst=list(str)
a=[]
b=[]
for i in range(0,len(str)):
    if i%2==0:
        a.append(lst[i])
    else:
        b.append(lst[i])
s1=''.join(a)
s2=''.join(b)
print(s1,s2)