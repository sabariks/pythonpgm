def small(l): 
     for i,n in enumerate(l):
         if n != '0':
             a = lst.pop(i) 
             break
 return (str(tmp) + ''.join(lst) ) 
 a=input()
 l=list(a)
 print(small(l))