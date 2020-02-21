l=[10]
l=map(int,input().split())
for i in range (0,10):
    if (l[i] < l[i+1]):
        print(l[i])
    else:
        print(l[i+1])

