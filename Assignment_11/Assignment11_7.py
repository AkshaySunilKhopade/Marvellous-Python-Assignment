i =0
def Display(no):
    global i
    # for i in range(0,no):
    #     for j in range(0,i):
    #         print("*",end = " ")
    #     print()
    
    j = 0
    if(i<no):
        j = 0
        while(j<=i):
            print("*",end=" ")
            j = j + 1
        print()
        i = i + 1
        Display(no)

        
        
def main():
    
    value = int(input("Enter the value : "))
    Display(value)
if __name__ == "__main__":
    main()