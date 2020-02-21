n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=[]
for i in range (0,n):
        if i % 2==0:
                b.append(max(a))
                a.remove(max(a))
        else:
                b.append(min(a))
                a.remove(min(a))
print(*b)
# b = map(str,b)
# print(''.join(b))