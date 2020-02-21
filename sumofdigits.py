n=input()
lst=list(n)
sum=0
val=1
for i in range(0,len(lst)):
    sum +=int(lst[i])
    val *=int(lst[i])
if val+sum==int(n):
    print('Great')
else:
    print('no')