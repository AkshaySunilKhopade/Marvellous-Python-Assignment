

iRet = lambda iNo : iNo**2


def main():
    print("Enter the value :")
    iNo = int(input())

    Power = iRet(iNo)
    print("Square is  : ",Power)


if __name__ == "__main__":
    main()