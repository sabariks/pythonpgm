n = int(input())
lst=[]

for i in range (0,n):
    if i==0:
        lst.append(800)
    c=2*i
    c=c+lst[i]
    if c<n:
        lst.append(c)
    else:
        break
lst.pop(0)
lst = map(str,lst)
ans = []
for i in lst:
    s = [int(i) for i in i]
    a = sum(s)
    ans.append(a)
ans = [str(i) for i in ans]
print(' '.join(ans))
count = 0 
for i in ans:
    l = [int(i) for i in i]
    if l[0]==1:
        count+=1
print(count)
