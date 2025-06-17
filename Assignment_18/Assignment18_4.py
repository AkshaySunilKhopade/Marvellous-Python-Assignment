import os 
import hashlib

def CheckSum(filename):
    
    fobj = open(filename,"rb")
    hobj = hashlib.md5()
    
    
    BLOCKSIZE = 1024
    buffer = fobj.read(BLOCKSIZE)
    
    while(len(buffer)>0):
        
        hobj.update(buffer)
        buffer = fobj.read(BLOCKSIZE)
    
    fobj.close()
    
    return hobj.hexdigest()


def DuplicateFile(filename1,filename2):
    flag1 = os.path.isabs(filename1)
    flag2 = os.path.isabs(filename2)
    
    if(flag1==False):
        filename1 = os.path.abspath(filename1)
    if(flag2==False): 
        filename2 = os.path.abspath(filename2)

    
    flag1 = os.path.exists(filename1)
    flag2 = os.path.exists(filename2)

    
    if(flag1==False):
        print("File Not Exist:",filename1)
        exit()
    if(flag2==False):
        print("File Not Exist:",filename2)
        exit()

    ret1 = CheckSum(filename1)
    ret2 = CheckSum(filename2)
    
    if(ret1==ret2):
        print("Files are Same")
    else :
        print("Files are differnet")

def main():
    
    print("Enter the file name :")
    filename1 = input()
    
    print("Enter the file name :")
    filename2 = input()
        
    
    DuplicateFile(filename1,filename2)
    
if __name__ == "__main__":
    main()
    


# CheckSum Genrattion Steps :
    
#     1. import hashlib library
#     2. open file in rb mode 
#     3. assign a varibale with hashlib.md5
#     4. read by buffer, 1st create buffer then read 
#     5. write a while loop for reading 
#     6. Before reading in loop 1st read upadte it to hobj.update(buffer)
#     7. return hobj.hexdigest()
