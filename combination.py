def prime(n):
    primes = 1
    while primes <= n:
            mod = 1
            ptrue = True
            while mod < 1:
                    if num%(num-mod) == 0:
                            ptrue = False
                            break
                    mod += 1
            if ptrue == True:
                    primes += 1
    return(primes)
nth = int(input())
print(prime(nth))