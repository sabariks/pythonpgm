st=input()
lst=list(st)
b = False
if st.isupper()==1 and len(st)==10:
    for i in range(0,5):
        b = True
else:
    b = False
if b==True:
    print('pan')
else:
    print('notpan')
