def XOR(n,a) : 
  
    ans = a[0] 
    for i in range(1,n) : 
        ans ^= a[i] 
          
    return ans 
n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=XOR(n,a)
print(b)