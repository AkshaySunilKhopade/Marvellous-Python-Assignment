

def Accept(size):
    print("Enter the Elements in List :")
    ino = 0
    data = list()
    
    for i in range(0,size):
        ino = int(input())
        data.append(ino)
        
    return data    

Double = lambda ino : ino * 2


def main():
    print("enter the size :")
    size = int(input())
    
    if((size==0) or (size < 0)):
        print("Enter the right size")
        return

    List = list()
    
    List = Accept(size)

    mdata = list(map(Double,List))
    print(mdata)
    
if __name__ == "__main__":
    main()