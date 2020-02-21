from collections import Counter
st=input()
mylist = list(st)
a=max(k for k,v in Counter(mylist).items() if v>1)
ls=[]

print(a)