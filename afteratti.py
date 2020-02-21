a=list(map(str,input().strip().split()))
art=['the','The','a','A','An','an']
ans=[]
for i in range(0,len(a)-1):
    if a[i] in art:
        ans.append(a[i+1])

if len(ans)==0:
    print('-1')
else:
    s =ans[0] 
    ans1 = []
    ans1.append(s.capitalize())
    for i in range(1,len(ans)):
        ans1.append(ans[i])
    print(' '.join(ans1))