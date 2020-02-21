n=int(input())
a=[]
b=[]
for i in range(2,n+1):
    if n%i==0:
        a.append(i)
n=a[0]
m=a[len(a)-1]
l=[]
for val in range(n,m): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           l.append(val)
prime=[]
for i in range(0,len(a)):
    if a[i] in l:
        prime.append(a[i])
prime.sort()
print(*prime)

