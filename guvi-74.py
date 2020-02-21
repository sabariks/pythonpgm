def rev(st):
    vol=['a','e','i','o','u','A','E','I','O','U']
    for x in st:
        if x in vol:
            st = st.replace(x,"")
    return st
n=int(input())
st=input()
lst=rev(st)
m=lst[::-1]
print(m)