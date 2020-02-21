m,n=map(int,input().split())
a=list(map(int,input().strip().split()))[:m]
# for i in range(0,nm):
#     if a[i]==n:
#         a.remove(a[i])
# print(len(a))

a.index += 1
print(a.index(min(a)))
