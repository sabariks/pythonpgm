
def cake(str):
    cost=0
    lst=list(str)
    for i in range(0,len(lst)-1):
        if lst[i]==lst[i+1] and lst[i]=='R':
            cost+=5
        elif lst[i]==lst[i+1] and lst[i]=='G':
            cost+=3
    return cost
m,n=map(int,input().split())
str1=input()
str2=input()
print(cake(str1)+cake(str2))
