m,n=map(str,input().split())
ls=list(m)
n=int(n)
ls1=ls[n:]+ls[:n]
print(''.join(ls1))