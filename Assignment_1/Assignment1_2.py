

def ChkNum(iNo):
    iAns = False

    if iNo < 0:
        iNo = -iNo
    
    if((iNo%2)==0):
        iAns = True
        return iAns
    else :
        return iAns

def main():
    iNo = 0
    print("Enter the Number :")
    iNo = int(input())
    
    iAns = False
    iAns = ChkNum(iNo)
    
    if(iAns == True):
        print("Number is Even")
    else :
        print("Number is Odd")

if __name__ == "__main__":
    main()