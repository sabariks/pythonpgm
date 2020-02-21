import re
st=input()
st1=input()
temp = re.findall(r'\d+', st)
res=list(map(int,temp))
s=sum(res)
temp1= re.findall(r'\d+', st1)
res1=list(map(int,temp1))
s1=sum(res1)
if s1 < s:
    a=len(st)-9
    print(st[:a])
else:
    b=len(st1)-9
    print(st1[:b])