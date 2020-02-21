st=input()
a=list(st)
lst=['c','e','r','s','u']
l=[]
for i in range(len(a)):
    if a[i] in lst:
        l.append(a[i])
if len(l) >=5:
    print('true')

