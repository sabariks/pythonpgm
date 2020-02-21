num=int(input())
l=list(str(num))
sum=int(l[len(l)-2])+int(l[len(l)-1])
for i in range(0,sum):
    b=0
    if sum== 4*i:
        b=1
if b==1:
    print('Yes')
else:
    print('No')
