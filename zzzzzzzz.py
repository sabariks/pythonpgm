# n=int(input())
# a=[]
# b=0
# for i in range(1,n):
#     x=n//i

#     if n%i==0 and x % 2!=0:
#         a.append(i)
#         b=1
# if b==1:
#     print(min(a))
# else:
#     print(1)


# n=int(input())
# l=[]
# for i in range(1,n+1):
#     val= (i**2) + 1
#     l.append(val)
# print(*l)

# import math 
# n=int(input())
# l=[]
# for i in range(0,n+1):
#     if i%2!=0:
#         l.append(math.factorial(i))
# print(*l)

# n=int(input())
# for  i in range(0,n+3):
#     for j in range(0,i):
#         print('1',end='')
#     print()    

# n=int(input())
# k=1
# for  i in range(1,n+1):
#     for j in range (1,k+1):
#         print("1",end="")
#     k=k+2
#     print("")


# st=input()
# a=len(list(st))
# b=len(set(st))*2
# print(b-a)


# import numpy as nm
# n=int(input())
# a=list(map(int,input().strip().split()))[:n]
# nm.argsort(a)

# b=[]
# for  i in range(0,len(a)):
#     b.append(a.index(max(a)))
#     a.remove(max(a))
# a.sort(reverse=True)
# print(b)


# n=int(input())
# A=list(map(int,input().strip().split()))[:n]
# B=A.sort()
# swaps = 0
# b = 1
# for a  in  range(1,len(A)):
#     if A[a] == B[b]:
#         b = b + 1
#     else:
#         swaps = swaps + 1


# n=int(input())
# a=[]
# b=[]
# for i in range(2,n+1):
#     if n%i==0:
#         a.append(i)
# n=a[0]
# m=a[len(a)-1]
# l=[]
# for val in range(n,m): 
#    if val > 1: 
#        for n in range(2, val): 
#            if (val % n) == 0: 
#                break
#        else: 
#            l.append(val)
# prime=[]
# for i in range(0,len(a)):
#     if a[i] in l:
#         prime.append(a[i])
# prime.sort()
# print(*prime)


# from itertools import count, filterfalse 
# n=int(input())
# a=list(map(int,input().strip().split()))[:n]
# b=min(set(xrange(1, len(a) + 1)) - set(a))
# print(b)


# def minNumber(a, n, x):  
#     a.sort(reverse = False) 
#     k = 0
#     while(a[int((n - 1) / 2)] != x): 
#         a[n - 1] = x 
#         n += 1
#         a.sort(reverse = False) 
#         k += 1
#     return k

# if __name__=='__main__':
#     n=int(input())
#     a=list(map(int,input().strip().split()))[:n]
#     x=int(input())
#     print(minNumber(a,n,x))



# st=input()
# a=list(st)
# b=len(st)//2
# if (a[0]=='a' or a[0]=='A') and (a[len(st)-1]=='W' or a[len(st)-1]=='w') and (a[b]=='m' or a[b]=='M'):
#     print(1)
# else:
#     print(-1)
# a=list(map(str,input().strip().split()))
# s=input()
# c=0
# for i in range(0,len(a)):
#     if a[i]==s:
#         c=c+1
# if c==0:
#     print('-1')
# else:
#     print(c)

#
# 
# 
# 
#  Python3 program to generate n-bit Gray codes 
import math as mt 
def generateGrayarr(n): 
	if (n <= 0): 
		return
	arr = list() 
	arr.append("0") 
	arr.append("1") 

	# Every iteration of this loop generates 
	# 2*i codes from previously generated i codes. 
	i = 2
	j = 0
	while(True): 

		if i >= 1 << n: 
			break
		for j in range(i - 1, -1, -1): 
			arr.append(arr[j]) 
		for j in range(i): 
			arr[j] = "0" + arr[j]  
		for j in range(i, 2 * i): 
			arr[j] = "1" + arr[j] 
		i = i << 1


print((*arr) )



generateGrayarr(3) 

 
