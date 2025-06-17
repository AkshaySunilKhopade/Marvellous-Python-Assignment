import os
import sys
import hashlib
import time


def CheckSum(path):
    
    fobj = open(path,"rb")
    hobj = hashlib.md5()
    BLOCKSIZE = 1024
    
    buffer = fobj.read(BLOCKSIZE)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(BLOCKSIZE)

    fobj.close()
    return hobj.hexdigest()


def FindDuplicate(Dirname):
    
    Duplicate = {}
    for Folder,SubFolders,Files in os.walk(Dirname):
        
        for filename in Files:
            filename = os.path.join(Folder,filename)
            checksum = CheckSum(filename)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(filename)
            else :
                Duplicate[checksum] = [filename]                                   
    
    return Duplicate

def DeleteDuplicate(Dirname):
    
    flag = os.path.isabs(Dirname)
    if(flag==False):
        Dirname=os.path.abspath(Dirname)
    flag = os.path.exists(Dirname)
    if(flag==False):
        print("Directory not exists")
        exit()
    flag = os.path.isdir(Dirname)
    if(flag==False):
        print("Given Name is not dir")

    MyDict = FindDuplicate(Dirname)
    Result = list(filter((lambda x : len(x)>1),MyDict.values()))

    Count = 0
    Cnt = 0
    data = list()
    
    for Key in Result:
        for values in Result:
            Count += 1
            if(Count>1):
                data.append(values)        
                os.remove(values)
                Cnt += 1
        Count = 0
    # print("Total Deleted files are :",Cnt)
    # print(data)

    # Log File Creation :
    
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
        fobj.write("\n")
    fobj.write(Border+"\n")
    
    
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("File Created at : "+timestamp+"\n")
    fobj.write(Border+"\n")
    
    fobj.close

def main():
    start_time = time.time()
    if((len(sys.argv))==2):
        if((sys.argv[1]=='--h') or (sys.argv[1]=='--H')):
            #Heading(Program Desc)
            print("Above Application is used to Find the duplicate values and delete them")
        
        elif((sys.argv[1]=='--u')or(sys.argv[1]=='--U')):
            print("Use the scriipt as :")
            print("Use cmd to give the input")    
        else :
            #Fucntion Call
            DeleteDuplicate(sys.argv[1])
    end_time = time.time()
    print("Required time for execution is :",end_time - start_time)


if __name__ == "__main__":
    main()