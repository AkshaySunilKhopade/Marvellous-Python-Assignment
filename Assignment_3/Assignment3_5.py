import MarvellousNum


def main():
    print("Enter the size :")
    iSize = int(input())

    data = list()
    print("Enter into List :")
    for i in range(0,iSize):
        value = int(input())
        ibool = MarvellousNum.ChkPrime(value)
        if(ibool):
            data.append(value)
    
    iRet = MarvellousNum.Addition(data)
    print(iRet) 

if __name__ == "__main__":
    main()