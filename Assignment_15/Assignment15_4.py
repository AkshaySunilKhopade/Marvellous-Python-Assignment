import os



def CompareFile(FileName1,Filename2):

    try :
        fd1 = open(FileName1,"r")
        fd2 = open(Filename2,"r")
        
        ret  = False
                
        data1 = fd1.read()
        data2 = fd2.read()
        
        if(data1 == data2): 
            ret = True    
        
    except Exception as eobj:
        print(eobj)

    return ret

def main():
    
    print("Enter the file name  1:")
    FileName1 = input()
    print("Enter the second filename")
    FileName2 = input()
    
    ret1 = os.path.exists(FileName1)
    ret2 = os.path.exists(FileName2)
    
    if(ret1==True and ret2==True):
        bool = CompareFile(FileName1,FileName2)
    else :
        print("File Not Exist")
    
    if(bool):
        print("Files are same")
    else :
        print("not same") 

if __name__ == "__main__":
    main()