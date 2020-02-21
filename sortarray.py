n=int(input())
a=[]
for i in range(0,n):
    s=input()
    a.append(s)
a.sort()
for i in range(0,n):
    print(a[i])
