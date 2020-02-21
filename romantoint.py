def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        # print('i value is ',i,'room value is ',rom_val[s[i]],'room value previous is ',rom_val[s[i-1]])
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            # print('int value is in if ',int_val)
        else:
            int_val += rom_val[s[i]]
            # print('int value is in else  ',int_val)
    return int_val

n = input()
try:
    print(roman_to_int(n))
except:
    print(-1)