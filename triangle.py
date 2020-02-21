def checkValidity(a, b, c):    
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return 'no'
    else: 
        return 'yes'
a,b,c=map(int,input().split())
print(checkValidity(a, b, c))