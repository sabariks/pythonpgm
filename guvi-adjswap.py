st=input()
n=len(st)
a=list(st)
for i in range(0,n-1):
    if i==0 or i%2==0:
        a[i],a[i+1]=a[i+1],a[i]
a = map(str,a)
print(''.join(a))