def CountFrequency(my_list): 
	freq = {} 
	for item in my_list: 
		if (item in freq): 
			freq[item] += 1
		else: 
			freq[item] = 1

	for key, value in freq.items(): 
		if value == 2:
			print(key)
n=int(input())
a=list(map(int,input().strip().split()))[:n]
CountFrequency(a) 