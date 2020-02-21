
def cmpa(x):
    st1=''.join(reversed(x))
    if x==st1:
        return ("yes")
    return ("no")
x=input()
print(cmpa(x))
