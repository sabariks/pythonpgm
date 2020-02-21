# def smalest_num(lst):
#     lst.sort()
#     if lst[0]!=1:
#         return 1
#     for i in range(1,n):
#         if lst[i] != lst[i-1]+1:
#             return lst[i-1]+1
#     if lst[n-1]==2**64-1:
#         assert('No gaps')
#     return lst[n-1]+1
# n=int(input())
# a=list(map(int,input().strip().split()))[:n]
# print(smalest_num(a))



from itertools import count, filterfalse # ifilterfalse on py2
n=int(input())
a=list(map(int,input().strip().split()))[:n]
print(next(filterfalse(set(a).__contains__, count(1))))