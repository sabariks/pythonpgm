a=list(map(str,input().strip().split()))
b=[]
for i in range(0,len(a)):
    # if i % 2==0:
        s=a[i]
        str = "" 
        for i in s:
            str = i + str
        b.append(str)
    # else:
    #     b.append(a[i])
print(*b)
