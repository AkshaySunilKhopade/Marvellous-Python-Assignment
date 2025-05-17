

def Display(iRow,iCol):
    for i in range(iRow,0,-1):
        for j in range(0,i):
            print("*",end = " ")
        print()

def main():
    print("Enter the row value :")
    row  = int(input())
    print("Enter the Column value :")
    col = int(input())
    Display(row,col)

if __name__ == "__main__":
    main()