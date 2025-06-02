from functools import reduce 

def Accept(iSize):
    data = list()
    print("Enter the values :")
    for i in range(0,iSize):
        no = int(input())
        data.append(no)
    return data

def Prime(iNo):
    iRet = True
    
    counter  = (int)(iNo/2 + 1)

    for i in range(2,counter):
        if(iNo%i==0):
            iRet = False

    return iRet

Multiply = lambda iNo : iNo*2

def Maximum(A,B):
    if(A > B):
        return A
    else :
        return B

def main():

    print("Enter the Size  :")
    iNo1 = int(input())

    data = Accept(iNo1)

    fdata = list(filter(Prime,data))
    print(fdata)
    mdata = list(map(Multiply,fdata))
    print(mdata)
    rdata = reduce(Maximum,mdata)
    print(rdata)
if __name__ == "__main__":
    main()