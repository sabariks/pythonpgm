n,m=map(int,input().split())
st=[]
for i in range (0,n):
    s=input()
    st.append(s)
for i in range(n-1):
    if st[m]==st[m+1] or st[m]==st[m-1]:
        print('yes')
        break
    else:
        print('no')
        break