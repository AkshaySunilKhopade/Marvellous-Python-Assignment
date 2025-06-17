import os 

def CheckFile(filename):
    
    flag = os.path.isabs(filename)

    if(flag==False):
        filename = os.path.abspath(filename)

    flag = os.path.isdir(filename)
    if(flag==True):
        print("It is Directory")
        exit()
    
    Ret = False
    
    flag = os.path.exists(filename)
    if(flag==True):
        Ret = True
    
    return Ret   

def main():
    
    print("Enter the file name :")
    filename = input()
    
    ret = CheckFile(filename)
    if(ret==True):
        print("File is present")
    else:
        print("File is not present")
if __name__ == "__main__":
    main()
    
