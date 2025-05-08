

def Add(iNo1,iNo2):
    iAns = 0
    iAns = iNo1 + iNo2
    return iAns

def main():
    iNo1 = 0
    iNo2 = 0
    
    print("Enter the First Number :")
    iNo1 = int(input())
    print("Enter the Second Number :")
    iNo2 = int(input())

    iAns = Add(iNo1,iNo2)
    print("Addition is :",iAns)


if __name__ == "__main__":
    main()