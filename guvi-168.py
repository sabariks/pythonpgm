n= int(input())
lst=[]
for i in range(n):
    st=input()
    lst.append(st)
    l=[]
for i in range(0,n-1):
    if lst[i]!=lst[i+1]:
        l.append(1)
    else:
        l.append(0)
a=set(l)
if ('0' in a) or len(a)==2:
    print('yes')
else:
    print('no')