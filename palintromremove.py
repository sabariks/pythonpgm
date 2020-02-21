def cmpa(x):
    st1=''.join(reversed(x))
    if x==st1:
        return ("yes")
    return ("no")
x=input()
b=list(x)
b.remove(b[len(b)-1])
a=''.join(b)
print(cmpa(a))