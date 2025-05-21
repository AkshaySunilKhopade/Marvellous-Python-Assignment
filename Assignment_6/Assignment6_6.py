

def Display(row):
    for i in range(1,row+1):
        for j in range(1,i):
            print("*",end = " ")
        print()        



def main():
    print("Enter the rows :")
    row = int(input())
    
    Display(row)

if __name__ == "__main__":
    main()
    
