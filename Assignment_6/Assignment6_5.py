

def Prime(iNo):
    bool = True
    iCnt = (int)(iNo/2)
    i = 2
    
    while(i<=iCnt):
        if((iNo%i)==0):
            bool = False 
        i = i+1    
    return bool



def main():
    print("Enter the number :")
    iNo = int(input())
    
    iPrime = Prime(iNo)
    if(iPrime):
        print("Prime")
    else : 
        print("Non Prime")
    

if __name__ == "__main__":
    main()
    
