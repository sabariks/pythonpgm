n=int(input())
b=0
for i in range(0,n):
    if pow(2,i)==n:
        b=1
if b==1:
    print('yes')
else:
    print('no')