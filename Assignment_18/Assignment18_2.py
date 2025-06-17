import os 

def PrintFile(filename):
    
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
        fobj = open(filename,"r")
        data = fobj.read()
        print(data)
    else:
        print("File is not present")    
    

def main():
    
    print("Enter the file name :")
    filename = input()
    
    PrintFile(filename)
    
if __name__ == "__main__":
    main()
    
