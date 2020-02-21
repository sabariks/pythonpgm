m,n=map(int,input().split())
l=[]
for val in range(n,m+1): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val)
print(l)
print(len(l))
