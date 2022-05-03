def isHamming(x):
    if(x==1):
        return 1
    if(x%2 == 0):
        return isHamming(x/2)
    if(x%3 == 0):
        return isHamming(x/3)
    if(x%5 == 0):
        return isHamming(x/5)

def hamming(x):
    if(x==1 ):
        return 1
    hamming(x-1)
    if(isHamming(x)):
        print("%d" % x)

if __name__ ==   '__main__':
    hamming(50)
