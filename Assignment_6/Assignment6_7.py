

def Accept(size):
    print("Enter the Elements in List :")
    ino = 0
    data = list()
    
    for i in range(0,size):
        ino = int(input())
        data.append(ino)
        
    return data    

def Largest(data) :
    ilag = 0
    for i in range(0,len(data)):
        if(data[i]>ilag):
            ilag = data[i]
    return ilag

def main():
    print("enter the size :")
    size = int(input())
    
    if((size==0) or (size < 0)):
        print("Enter the right size")
        return

    List = list()
    
    List = Accept(size)

    Ret = Largest(List)
    print("Lagerst element is :",Ret)

if __name__ == "__main__":
    main()