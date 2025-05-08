
def ChkDiv(iNo):
    iAns = False

    if((iNo%5)==0):
        iAns = True
    else :
        iAns = False

    return iAns


def main():
    iNum = 0
    iAns = False

    print("Enter the Number :")
    iNum = int(input())

    iAns = ChkDiv(iNum)

    if(iAns):
        print("Number is Divisible by 5")
    else :
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()