import math

def isPerfectSquare(x) :
    sr = math.sqrt(x)
    return((sr*sr) == x)

while 1 :

    nBulb = int(input())
    if nBulb == 0 :
        break
    if nBulb == 1 :
        print('Yes')
    if isPerfectSquare(nBulb):
        print('Yes')
    else :
        print('No')
    
    


