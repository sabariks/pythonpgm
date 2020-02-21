def cmpa(x):
    st1=''.join(reversed(x))
    if x==st1:
        return ("yes")
    return ("no")
x=int(input())
sum=0
lst=list(str(x))
for i in range(0,len(lst)):
    a=int(lst[i])
    sum += a
st=str(sum)
print(cmpa(st))