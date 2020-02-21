from itertools import permutations 
  
def allPermutations(str):  
     permudation = permutations(str) 
     for perm in list(permudation): 
         print (''.join(perm)) 
        
if __name__ == "__main__": 
    str = input()
    allPermutations(str) 