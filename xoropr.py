m,n=map(int,input().split())
a=m^n
b=bin(a)[2:]
s= [ones for ones in b if ones=='1'] 
print(len(s))