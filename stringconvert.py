st1,st2=map(str,input().split())
l1=list(st1)
l2=list(st2)
for i in range(0,len(st1)):
    if l1[i] in l2:
        l2.remove(l1[i])
print(len(l2))