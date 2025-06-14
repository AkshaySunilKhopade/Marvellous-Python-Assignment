import os

def main():
    
    print("Enter the file name :")
    fd = input()
    
    ret = os.path.exists(fd)
    
    if(ret==True):
        print("File Exists")
    else :
        print("File Not Exists")

if __name__ == "__main__":
    main()