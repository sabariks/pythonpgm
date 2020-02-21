m,n=map(int,input().split())
a=max(m,n)
for i in range(1,a+1):
    if i%m==0 and i%n==0:
        print(i)
        