st=list(map(str,input()))
st1=list(map(str,input()))
b=[]
for i in range(len(st)):
    if st[i]!=st1[i]:
        break
    else:
        b.append(st[i])
print(''.join(b))