a=int(input())
b=list(str(a))
n=len(b)
sum=0
for i in range(0,n):
    x=int(b[i])
    sum+=pow(x,n)
print(sum)

