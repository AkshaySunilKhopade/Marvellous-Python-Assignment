

def Factorial(iNo):
    iFact = 1
    while(iNo > 0):
        iFact = iFact * iNo
        iNo = iNo - 1 
    return iFact



def main():
    print("Enter the number :")
    iNo = int(input())
    
    iFact = Factorial(iNo)
    print("Factorial is :",iFact)
    

if __name__ == "__main__":
    main()
    
