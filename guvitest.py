x=int(input())
if x==16:
    def getdigit(digs):
        dig=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        for x in range(len(dig)):
            if digs==dig[x]:
                return x
    def hextodec(num):
        dec=0
        p=0
        n=list(num)
        n.reverse()
        for i in range(0,len(n)):
            x=getdigit(n[i])
            dec = dec + 16 ** p * x
            p+=1
        print(str(dec))
    a=input()
    hextodec(a)
else:
    num=int(input())
    dec=0
    p=0
    n=list(str(num))
    n.reverse()
    for i in range(0,len(n)):
        dec = dec + int(n[i]) ** p * x
        p+=1
    print(str(dec))
