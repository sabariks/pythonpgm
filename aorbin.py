st=input()
lst=list(st)
a=[]
for i in range(0,len(st)):
    if lst[i] =='a' or lst[i]=='b':
        a.append(1)
if len(a)==len(lst):
    print('yes')
else:
    print('no')
