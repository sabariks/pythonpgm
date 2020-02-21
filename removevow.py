s=input()
c=list(s)
vowels=['A','a','E','e','I','i','O','o','U','u']
bol=0
for i in range(0,len(s)):
    if c[i] in vowels:
        bol=1
if bol==1:
    print('yes')
else:
    print('no')


# abc = ''.join([l for l in c if l not in vowels])
# abc = [i for i in abc]
# print(''.join(abc))