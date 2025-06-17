import os 

def Search(filename,str):
    
    flag = os.path.isabs(filename)

    if(flag==False):
        filename = os.path.abspath(filename)

    flag = os.path.isdir(filename)
    if(flag==True):
        print("It is Directory")
        exit()
    
    
    flag = os.path.exists(filename)
    
    if(flag==False):
        print("File not exists")
    
    fobj = open(filename,"r")
    count = 0
    
    for line in fobj:
        sent = line.split()
        for i in range(0,len(sent)):
            # print(sent[i])
            if(str == sent[i]):
                count += 1
    
    print("Count of occured string is :",count)            

def main():
    
    print("Enter the file name :")
    filename = input()
    print("Enter the string to seach :")
    str = input()
    Search(filename,str)
    
if __name__ == "__main__":
    main()
    
