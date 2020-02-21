a=list(map(str,input().strip().split()))
lst=[]
for i in range(0,len(a)):
    m=len(a[i])
    lst.append(m)
for i in range(0,len(a)):
    if len(a[i])==max(lst):
        print(a[i])
        break
