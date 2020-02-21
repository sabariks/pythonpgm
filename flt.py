s=int(input())
lst=[]
for i in range (0,s):
    b=input()
    lst.append(b)
    lst.sort()
for i in range (0,s):
    print(lst[i])

