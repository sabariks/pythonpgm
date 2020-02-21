# import math 
# n=int(input())
# for i in range(0,n):
#     if i%2!=0:
#         print(math.factorial(i),end=" ")
# m=int(input())
# x=list(map(int,input().strip().split()))[:m]
# for i in range(0,m):
#     a=chr(x[i])
#     print(a)



# n=int(input())
# l=[]
# for val in range(n): 
#    if val > 1: 
#        for n in range(2, val): 
#            if (val % n) == 0: 
#                break
#        else: 
#            l.append(val)
# print(*l)
# c=0
# for i in range(0,len(l)):
#     for j in range (0,len(l)):
#         a=l[i]+l[j]
#         print(a)
# print(c)
def is_camel_case(s):
    return s != s.lower() and s != s.upper() and "_" not in s
s=input()
if is_camel_case(s)==True:
    print('yes')
else:
    print('no')