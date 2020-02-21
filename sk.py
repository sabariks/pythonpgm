s=input()
a=list(s)
s=0
for i in range (0,len(a)):
    b=ord(a[i])
    if (a==97) or (a==101)or (a==105) or (a==111) or (a==117):
        s+=a
        if (s%8==0):
            print(1)
        else:
            print(0)
    else:
        print(0)
        break

