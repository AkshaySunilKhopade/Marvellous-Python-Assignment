

def Display(iRow,iCol):
    for i in range(0,iRow):
        for j in range(1,iCol+1):
            print(j,end = " ")
        print()

def main():
    print("Enter the row value :")
    row  = int(input())
    print("Enter the Column value :")
    col = int(input())
    Display(row,col)

if __name__ == "__main__":
    main()