n=int(input())
a=list(map(str,input().strip().split()))[:n]

b=list(map(str,input().strip().split()))[:n]
a.reverse()
if (a==b):
    print('yes')
