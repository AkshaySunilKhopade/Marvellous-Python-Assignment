
def Display(iCnt):
    for i in range(0,iCnt):
        print("*",end=" ")

def main():
    iCnt = 0
    print("Enter the no of star to print :")
    iCnt = int(input())

    Display(iCnt)

if __name__ == "__main__":
    main()