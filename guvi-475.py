import re
def emax(str1):
    n=re.findall("\d+",str1)
    return n
s=input()
lst=emax(s)
l = [int(i) for i in lst]
print(max(l))