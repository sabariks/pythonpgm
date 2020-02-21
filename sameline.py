ls1=list(map(int,input().strip().split()))[:2]
ls2=list(map(int,input().strip().split()))[:2]
ls3=list(map(int,input().strip().split()))[:2]
# a=ls1+ls2+ls3
# def collinear(x1, y1, x2, y2, x3, y3): 
#     b = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
  
#     if (b == 0): 
#         print ("yes")
#     else: 
#         print ("no")



for i in range(2):
    m=1
    if ls1[i]==ls2[i] and ls2[i]==ls3[i]:
        m=0
if m==0:
     print('yes')
else:
    print('no')
