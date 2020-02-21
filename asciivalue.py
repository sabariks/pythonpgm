s=input()
l=list(s)
sum=0
for i in range(0,len(s)):
    val=ord(l[i])
    sum+=val
print(sum)
