

def Factorial(iNo):
    iRet = 1
    
    if iNo == 0:
        return 1
    
    for i in range(1,iNo+1):
        iRet = iRet * i

    return iRet

def main():
    print("Enter the value :")
    iNo = int(input())

    iResult = Factorial(iNo)  
    print(iResult)

if __name__ == "__main__":
    main()