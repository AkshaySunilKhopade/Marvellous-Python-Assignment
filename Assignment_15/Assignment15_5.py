import os

def CompareFile(FileName,str):
    no = 0
    try :
        fd1 = open(FileName,"r")
        strlen = len(str)
        size = os.path.getsize(FileName)
        
        for i in fd1:
            data = i
            if str in data:
                no = no + 1
                #print("found")
            
        return no    
    
    except Exception as eobj:
        print(eobj)

     

def main():
    
    print("Enter the file name  1:")
    FileName1 = input()
    print("Enter the stirng")
    str = input()
    
    ret1 = os.path.exists(FileName1)
    
    if(ret1==True):
        ret = CompareFile(FileName1,str)
    else :
        print("File Not Exist")
        return
    
    print("Present for times : ",ret)
    
if __name__ == "__main__":
    main()