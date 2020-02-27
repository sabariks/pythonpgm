import math
a,b,c=map(int,input().split())
if (-b+math.sqrt((b**2)-(4*a*c)))%(2*a)==0:
	x1=(-b+math.sqrt((b**2)-(4*a*c)))//(2*a)
else:
  x1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
if (-b-math.sqrt((b**2)-(4*a*c)))%(2*a)==0:
	x2=(-b-math.sqrt((b**2)-(4*a*c)))//(2*a)
else:
  x1=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
print('%.2f'%x1)
print('%.2f'%x2)
