st=input()
a=list(st)
lst1=['a','e','i','o','u']
l=[]
b=[]
for i in range(len(a)):
    if a[i] in lst1:
        l.append(a[i])
    else:
       
        b.append(a[i])
print(''.join(l)+''.join(b))