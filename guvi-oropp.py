def OR(n,a) : 
  
    ans = a[0] 
    for i in range(n) : 
        ans |= a[i] 
          
    return ans 
n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=OR (n,a)
print(b)