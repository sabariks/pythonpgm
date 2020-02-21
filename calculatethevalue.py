n=int(input())
l=list(str(n))
sum=int(l[0])**0
for i in  range(1,len(l)):
    sum+=int(l[i])**int(l[i-1])
    print(sum)
print(sum)
