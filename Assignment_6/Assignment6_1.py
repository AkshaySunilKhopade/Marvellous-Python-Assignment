

def Display(iNo):
    iCnt = 1
    while(iCnt<=iNo):
        print(iCnt,end = " ")
        iCnt = iCnt + 1    



def main():
    print("Enter the Number(Limit) :")
    iNo = int(input())
    
    Display(iNo)
    

if __name__ == "__main__":
    main()