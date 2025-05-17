

def Display(iRow,iCol):
    for i in range(1,iRow+1):
        for j in range(1,i+1):
            print(j,end = " ")
        print()

def main():
    print("Enter the row value :")
    row  = int(input())
    print("Enter the Column value :")
    col = int(input())
    print()
    Display(row,col)

if __name__ == "__main__":
    main()