

b=input()

a=list()
l=0
m=1
for i in range(0,len(a)):
    l+=a[i]
    m*=a[i]
sum=m+l
if sum < int(b):
    print('Great')
else:
    print('no')