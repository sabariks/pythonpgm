m,n=map(int,input().split())
sum=0
for i in range(m,n):
    if i % 2!=0:
        sum += i
print(sum)