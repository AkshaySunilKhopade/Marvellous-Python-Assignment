

def Prime(iNo):
    iRet = True
    
    counter  = (int)(iNo/2 + 1)

    for i in range(2,counter):
        if(iNo%i==0):
            iRet = False

    return iRet

def main():
    print("Enter the value :")
    iNo = int(input())

    iResult = Prime(iNo)  
    if(iResult):
        print("Number is Prime")
    else : 
        print("Number is not Prime")
if __name__ == "__main__":
    main()