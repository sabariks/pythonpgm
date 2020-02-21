a=list(map(str,input().strip().split()))
print(a)
for i in range (1,len(a)):
    if a[i]=='and':
        a[i-1],a[i+1]=a[i+1],a[i-1]
a = map(str,a)
print(' '.join(a))