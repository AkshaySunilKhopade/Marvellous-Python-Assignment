

def FactAddtion(iNo):
    iRet = 0
    
    if iNo == 0:
        return 0
    
    counter  = (int)(iNo/2 + 1)

    for i in range(1,counter):
        if(iNo%i==0):
            iRet = iRet + i

    return iRet

def main():
    print("Enter the value :")
    iNo = int(input())

    iResult = FactAddtion(iNo)  
    print(iResult)

if __name__ == "__main__":
    main()