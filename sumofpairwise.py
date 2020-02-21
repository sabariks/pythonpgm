def getPairsCount(arr, n, sum): 
    count = 0 
    for i in range(0, n): 
        for j in range(0, n): 
            if arr[i] + arr[j] == sum: 
                count += 1
    return count 
n=int(input())
arr=[]
for i in range(1,n):
    arr.append(i)
print(getPairsCount(arr,n-1,n))