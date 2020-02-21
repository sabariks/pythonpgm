st=input()
lst = list(st)
l=[lst[0]]
for i in range(1,len(lst)):
    if i%3==0:
        l.append(lst[i])
print(''.join(l))