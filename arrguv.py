n=int(input())
a=list(map(int,input().strip().split()))[:n]
s=0
for i in range(0,n):
    s+=a[i]
if s%2==0 and s%3==0 and s%5==0:
    print('1')
else:
    print('0')




    s=input()
lst=list(s)
for i in range (0,n):
    a=ord(a[i])
print(lst)

