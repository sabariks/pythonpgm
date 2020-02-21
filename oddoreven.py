n=int(input())
a=list(str(n))
sum=0
for i in range(0,len(a)):
    sum += int(a[i])
if sum % 2 == 0:
    print('E')
else:
    print('O')  