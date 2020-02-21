n=int(input())
ls=list(str(n))
a=[]
for i in range(len(ls)):
    val=pow(int(ls[i]),2)
    a.append(val)
print(sum(a))
