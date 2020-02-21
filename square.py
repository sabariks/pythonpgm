import math
def distance(p1,p2,p3,p4):
    val=(p2-p1)**2+(p4-p3)**2
    d=math.sqrt(val)
    return d
ls1=list(map(int,input().strip().split()))[:2]
ls2=list(map(int,input().strip().split()))[:2]
ls3=list(map(int,input().strip().split()))[:2]
ls4=list(map(int,input().strip().split()))[:2]
v1=distance(ls1[0],ls1[1],ls2[0],ls2[1])
v2=distance(ls2[0],ls2[1],ls3[0],ls3[1])
v3=distance(ls3[0],ls3[1],ls4[0],ls4[1])
v4=distance(ls4[0],ls4[1],ls1[0],ls1[1])
if v1==v2==v3==v4:
    print('yes')
else :
    print('no')