
def Digits(iNo):

    if iNo == 0:
        return 0
    
    temp = iNo    
    iSum =0


    while(temp != 0):
        idigit = (int)(temp % 10)
        temp = (int)(temp/10)
        iSum = iSum + idigit
        print(idigit)

    return iSum


def main():
    print("Enter the number :")
    iNo = int(input())
    
    iRet = Digits(iNo)
    print(iRet)

if __name__ == "__main__":
    main()