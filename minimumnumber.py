n=int(input())
m=int(input())
lst=list(str(m))
for i in range(0,n):
    lst.remove(max(lst))
print(''.join(lst))