
def ChkNum(iNo):
    if(iNo > 0):
        print("Posiitve")
    elif(iNo<0):
        print("Negative")
    else : 
        print("Zero")

def main():
    iNo = 0
    
    print("Enter the Number :")
    iNo = int(input())

    ChkNum(iNo)


if __name__ == "__main__":
    main()