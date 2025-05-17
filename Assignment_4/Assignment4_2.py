

iRet = lambda iNo1,iNo2 : iNo1*iNo2


def main():
    print("Enter the value1 :")
    iNo1 = int(input())

    print("Enter the value2 :")
    iNo2 = int(input())

    Mul = iRet(iNo1,iNo2)
    print("Multiplication  is  : ",Mul)


if __name__ == "__main__":
    main()