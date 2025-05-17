def Addition(data):
    iSum = 0

    if(len(data)==0):
        return 0
    
    for i in range(0,len(data)):
        iSum +=data[i]

    return iSum

def ChkPrime(iNo):
    iRet = True
    
    counter  = (int)(iNo/2 + 1)

    for i in range(2,counter):
        if(iNo%i==0):
            iRet = False

    return iRet

