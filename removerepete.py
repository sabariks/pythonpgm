a=list(map(str,input().strip().split()))
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            a.remove(a[i])
            a.remove(a[j])
            print(a[j])
print(a)