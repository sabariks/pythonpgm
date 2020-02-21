from statistics import median
m=int(input())
a=list(map(int,input().split()))[:m]
n=int(input())
import statistics 

print("Median of data-set is : % s "
        % (statistics.median(a)))