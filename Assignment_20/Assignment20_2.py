import sys
import time
import os
import schedule
import hashlib



def CalculateCheckSum(path,BlockSize=1024):
         
    fobj = open(path,"rb")
    
    hobj = hashlib.md5()
    
    buffer = fobj.read(BlockSize)
    
    while(len(buffer)>0):
        
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)
        
    fobj.close()

    return hobj.hexdigest()    


def Traversal(DirName):
    
    flag = os.path.isabs(DirName)
    if(flag==False):
        DirName = os.path.abspath(DirName)
        
    ret = os.path.exists(DirName)
    
            
    if(ret==False):
        print("The Path is invalid ")
        exit()
        
    flag = os.path.isdir(DirName)
    if(flag==False):
        print("PAth is valid but the target is not directory")
        exit()
            
    # print("Absolute path is : "+DirName)

    for FolderName,SubFolder,Files in os.walk(DirName):
        
        for filename in Files :
            # filename = FolderName+"/"+filename
            filename = os.path.join(FolderName,filename)
            checksum = CalculateCheckSum(filename)
            # print("File name :",filename,end=" ")
            # print("",checksum)
            # print()
                                    
    
# copy down

def FindDuplicate(DirName):
    
    flag = os.path.isabs(DirName)
    if(flag==False):
        DirName = os.path.abspath(DirName)
        
    ret = os.path.exists(DirName)
    
            
    if(ret==False):
        print("The Path is invalid ")
        exit()
        
    flag = os.path.isdir(DirName)
    if(flag==False):
        print("PAth is valid but the target is not directory")
        exit()
            
    # print("Absolute path is : "+DirName)

    Duplicate = {}                   #Dict used to store the checksum and file name and assign 
    for FolderName,SubFolder,Files in os.walk(DirName):
        
        for filename in Files :
            # filename = FolderName+"/"+filename
            filename = os.path.join(FolderName,filename)
            checksum = CalculateCheckSum(filename)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(filename)
            else :
                Duplicate[checksum] = [filename]                                   
    
    
    return Duplicate

def DisplayResult(MyDict):
    
    Result = list(filter(lambda X : len(X)>1,MyDict.values()))
    # print(Result)
    
    Count = 0
    
    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        print("------------------------------")
        print("Value of Count is :",Count)
        print("------------------------------")
        Count = 0           

def DeleteDuplicate(path="Test"):
    
    MyDict = FindDuplicate(path)
    Result = list(filter(lambda X : len(X)>1,MyDict.values()))
    # print(Result)
    
    Count = 0
    Cnt = 0
    data = list()
    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Delete value :",subvalue)
                data.append(subvalue)

    Border = "-"*54
    timestamp = time.ctime()
    #print(timestamp)
    

    filename = "MarvellousLog_%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    #print(filename)
    
    fobj = open(filename,"w")
    fobj.write(Border+"\n")
    fobj.write("Deleted Files are :")
    for i in range(0,len(data)):
        fobj.write(data[i])
        print()
    fobj.write(Border+"\n")
    
    
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("File Created at : "+timestamp+"\n")
    fobj.write(Border+"\n")
    
    fobj.close

            
def main():
    Border = "-"*54
    print(Border)
    print("_________________MARVELLOUS AUTOMATION________________")
    print(Border)

    #logic
    
    if((len(sys.argv)==2)):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform-----")
            print("This is the automation script")

        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("use the given script as ")
            print("ScriptName.py Argument1 Arguement2")
    
    if((len(sys.argv)==3)):
            #logic            
            # Traversal(sys.argv[1])
            # result = FindDuplicate(sys.argv[1])

            schedule.every(int(sys.argv[2])).minutes.do(DeleteDuplicate,)
            
            while(True):
                schedule.run_pending()
                time.sleep(1)
    else :
        print("Invalid no of arguements")
        print("Use the given flags as :")
        print("--h to display the help")
        print("--u to display the usage")
        
        


    print(Border)
    print("_____________Thank you for using our script___________")
    print("_________________MARVELLOUS INFOSYSTEMS_______________")
    print(Border)
   


if __name__ == "__main__":
    main()
    
# steps :
#     1. Check path is absolute or not os.path.isab()
#     2. If path is not absolute the make it using os.path.abspath()
#     3. Check path exists or not os.path.exists() if not then exit
#     4. then check if its directory or not ,if not then exit 
    