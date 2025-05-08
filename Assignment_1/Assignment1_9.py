
def Display(iNo):
    iNo = iNo*2 + 1
    for i in range(1,iNo):
        if(i%2==0):
            print(i,end=" ")


def main():
    iNo = 0

    print("Enter the Value :")
    iNo = int(input())

    Display(iNo)


if __name__ == "__main__":
    main()