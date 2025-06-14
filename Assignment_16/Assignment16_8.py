import os


def Calculate(Filename):
    flag = os.path.isabs(Filename)
    if(flag==False):
        Filename = os.path.abspath(Filename)
        
    ret = os.path.exists(Filename)
    
            
    if(ret==False):
        print("The Path is invalid ")
        exit()
        
    flag = os.path.isdir(Filename)
    if(flag==True):
        print("PAth is valid but the target is not directory")
        exit()
            
    print("Absolute path is : "+Filename)
    
    # word = 0
    # rline = 0
    # character = os.path.getsize(Filename)
    
    fobj = open(Filename,"r")
    fobj2 = open("Maarvellous.txt","w")
    for line in fobj:
        if line.strip() != "":
            fobj2.write(line)

def main():
    print("enter the file name: ")
    FileName = input()
    
    Calculate(FileName)

if __name__ == "__main__":
    main()