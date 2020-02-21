n=int(input())
a=[]
b=[]
for i in range(2,n+1):
    if n%i==0:
        a.append(i)
print(a)
