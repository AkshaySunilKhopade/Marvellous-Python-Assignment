

def Accept(size):
    print("Enter the Elements in List :")
    ino = 0
    data = list()
    
    for i in range(0,size):
        ino = int(input())
        data.append(ino)
        
    return data    

Even = lambda ino : (ino % 2 ==0)


def main():
    print("enter the size :")
    size = int(input())
    
    if((size==0) or (size < 0)):
        print("Enter the right size")
        return

    List = list()
    
    List = Accept(size)

    fdata = list(filter(Even,List))
    print(fdata)
    
if __name__ == "__main__":
    main()