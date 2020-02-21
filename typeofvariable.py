n=int(input())
if n >= 2**63-1:
    print('LONG')
else:
    print('INT')