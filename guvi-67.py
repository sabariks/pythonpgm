s=str(input())
l=list(s)
lst=[]
for i in range(len(l)):
    if i%2==0:
        lst.insert(i,l[i])
    else:
        lst.insert(i-1,l[i])
print(''.join(lst))

