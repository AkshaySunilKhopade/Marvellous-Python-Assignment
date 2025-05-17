
def Digits(iNo):

    if iNo == 0:
        return 0
    
    temp = iNo    
    counter =0


    while(temp != 0):
        idigit = (int)(temp % 10)
        temp = (int)(temp/10)
        counter = counter + 1
        print(idigit)

    return counter


def main():
    print("Enter the number :")
    iNo = int(input())
    
    iRet = Digits(iNo)
    print(iRet)

if __name__ == "__main__":
    main()