import os

def WritingIntoFile(FileName):
    print("Welcome to Function")
    try :
        fd1 = open(FileName,"r")
        fd2 = open("hello.txt","w")
    
        data = fd1.read()
        fd2.write(data)
        print("Data writen successfully")
        
    except Exception as eobj:
        print(eobj)


def main():
    
    print("Enter the file name :")
    FileName = input()
    
    ret = os.path.exists(FileName)
    if(ret==True):
        WritingIntoFile(FileName)
    else :
        print("File Not Exist")

if __name__ == "__main__":
    main()