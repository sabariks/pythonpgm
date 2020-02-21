st=list(map(str,input().split()))
st2=str(input())
if st2 in st:
    st.remove(st2)
    print(' '.join(st))
else:
    print(' '.join(st))