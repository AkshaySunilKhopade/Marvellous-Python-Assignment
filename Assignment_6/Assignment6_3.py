

def Display(iNo):
    iCnt = 1
    while(iCnt<=10):
        print(iNo,"x",iCnt,"=",iNo*iCnt,)
        iCnt = iCnt + 1    



def main():
    print("Enter the Number(Limit) :")
    iNo = int(input())
    
    Display(iNo)
    

if __name__ == "__main__":
    main()