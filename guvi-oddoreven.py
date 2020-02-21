
def fun(n):
    if n <= 3:
        return 0
    if (n%2==0 or n%3==0):
        return 1
    i=5
    while(i*i<=n):
        if (n%i==0 or n%(i+2)==0):
            return 1
        i=i+6
    return 0
n=int(input())
if fun(n)==1:
    print('yes')
else:
    print('no')