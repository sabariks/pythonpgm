def mulof(a):
    for i in range(1,int(a/10)):
        b=pow(7,i)
        if a==b:
            a=1
    return a
a=int(input())
c=mulof(a)
if c==1:
    print('yes')
else:
    print('no')