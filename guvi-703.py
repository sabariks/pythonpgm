import re
str=input()
list=list(str)
pattern = '[0-9]'
list = [re.sub(pattern, '', i) for i in list] 
c=[]
for i in str:
        if i.isdigit():
            c.append(int(i))
a=sum(c)
print('sa is ',a)
e = 5
b = str(e)

# print(type(b))
# print(list)
# print(''.join(list))