

def Display(iNo):
    iCnt = 1
    iSum = 0
    while(iCnt<=iNo):
        if((iCnt % 2)==0):
            iSum = iSum + iCnt
        iCnt = iCnt + 1
    return iSum


def main():
    print("Enter the Number(Limit) :")
    iNo = int(input())
    
    Sum = Display(iNo)
    print("Sum is :",Sum)
    

if __name__ == "__main__":
    main()