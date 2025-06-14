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
    
    word = 0
    rline = 0
    character = os.path.getsize(Filename)
    
    fobj = open(Filename,"r")
    
    for line in fobj:
        word1 = len(line.split())
        word += word1
        rline = rline +1       

    print(word,rline,character)


def main():
    print("enter the file name: ")
    FileName = input()
    
    Calculate(FileName)

if __name__ == "__main__":
    main()