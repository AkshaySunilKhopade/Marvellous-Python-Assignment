import os
import sys
import hashlib
import time
import send_email
import datetime


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
    Count = 0
    for Folder,SubFolders,Files in os.walk(Dirname):
        
        for filename in Files:
            filename = os.path.join(Folder,filename)
            Count +=1
            # print(filename)
            checksum = CheckSum(filename)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(filename)
            else :
                Duplicate[checksum] = [filename]                                   
    # print(Duplicate)
    return Duplicate,Count


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

    # print(Dirname)
    MyDict,CountFiles = FindDuplicate(Dirname)
    # print(MyDict)
    Result = list(filter((lambda x : len(x)>1),MyDict.values()))
    Count = 0
    # print(Result)
    Cnt = 0
    data = list()
    
    for Key in Result:
        for values in Key:
            Count += 1
            if(Count>1):
                print(values)
                data.append(values)        
                # os.remove(values)
                Cnt += 1
        Count = 0
    # print("Total Deleted files are :",Cnt)
    return data,CountFiles

# Log File Creation :
    
def CreateLog(Dirname):    
    Border = "-"*54
    timestamp = time.ctime()
    #print(timestamp)
    
    Folder = "Marvellous"
    flag = os.path.exists(Folder)
    if(flag==False):
        os.mkdir(Folder)
        
    filename = Folder+"/MarvellousLog_%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    #print(filename)
    
    data,Count = DeleteDuplicate(Dirname)
    
    fobj = open(filename,"w")
    fobj.write(Border+"\n")
    fobj.write("Deleted Files are :")
    fobj.write("\n")
    fobj.write(Border+"\n")

    for i in range(0,len(data)):
        fobj.write(data[i])
        fobj.write("\n")
    fobj.write("\n")
    fobj.write("Total File Scanned are : ")
    fobj.write(str(Count))
    fobj.write("\n")
    fobj.write("Total Deleted are : ")
    deleted = str(len(data))
    fobj.write(deleted)
    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("File Created at : "+timestamp+"\n")
    fobj.write(Border+"\n")
    
    fobj.close
    return filename,Count,deleted

