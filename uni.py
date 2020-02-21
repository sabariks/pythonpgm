s= input()
b=''.join(i for i in s if i.isdigit())
c=str(b)
list=list(c)
s=0
for i in range(0,len(list)):
    s=s+int(list[i])
print(s)