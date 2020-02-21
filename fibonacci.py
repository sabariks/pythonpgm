#fibonacci series
def fibo(a):
    if a<=1:
        return a
    else:
        return (fibo(a-1)+fibo(a-2))
b=int(input())
if b<=0:
    print("Enter valid Number!")
else:
    for i in range(b):
        print(fibo(i))
