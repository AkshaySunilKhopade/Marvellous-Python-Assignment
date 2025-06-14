import os
import sys

def ReadData(Filename):
    
    flag = os.path.isabs(Filename)

    if(flag == False):
        Filename = os.path.abspath(Filename)
    
    flag = os.path.exists(Filename)
    if(flag == False):
        print("File doesnt exists")
        exit()
        
    fd = open(Filename,"r")
    data = fd.read()
    
    print(data)

def main():
    
    print("Enter the file to open :")
    Filename = input()
    
    ReadData(Filename)

if __name__ =="__main__":
    main()