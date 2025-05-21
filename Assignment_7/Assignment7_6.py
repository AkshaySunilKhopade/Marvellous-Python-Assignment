def Accept(size):
    print("Enter the Elements in List :")
    ino = 0
    data = list()
    
    for i in range(0,size):
        ino = int(input())
        data.append(ino)
        
    return data    


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
    print("enter the size :")
    size = int(input())
    
    if((size==0) or (size < 0)):
        print("Enter the right size")
        return

    List = list()
    
    List = Accept(size)

    fdata = list(filter(Prime,List))
    print(fdata)
    
if __name__ == "__main__":
    main()