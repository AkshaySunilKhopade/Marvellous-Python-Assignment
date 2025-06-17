import sys
import os
import hashlib
import time

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

def FindDuplicate(DirName):
    
        
    Duplicate = {}

    for Folder, SubFolder, Files in os.walk(DirName):
        
        for filename in Files :
            filename = os.path.join(Folder,filename)
            checksum = CheckSum(filename)
            #condition for checking if already presemt in dict
            
            if checksum in Duplicate:
                Duplicate[checksum].append(filename)
            else :
                Duplicate[checksum] = [filename]  
        # print(Duplicate)     
    
    return Duplicate




def DeleteDupliacte(DirName):
    
    flag = os.path.isabs(DirName)
    if(flag==False):
        DirName = os.path.abspath(DirName)
    
    flag = os.path.exists(DirName)
    if(flag==False):
        print("Directory Not Exists")
        exit()
        
    flag = os.path.isdir(DirName)
    if(flag==False):
        print("It is not directory")
        exit()
    
    MyDict = FindDuplicate(DirName)
    #filter we should here as it will filter the values if their are more than one value
    Result = list(filter((lambda X:len(X)>1),MyDict.values()))
    # print(Result)
    Count = 0
    Cnt = 0
    data = list()
    
    for checksums in Result:
        for values in checksums:
            Count += 1
            if Count > 1:
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
    
    if((len(sys.argv))==2):
        if((sys.argv[1]=='--h') or (sys.argv[1]=='--H')):
            #Heading(Program Desc)
            print("Above Application is used to Find the duplicate values and delete them")
        
        elif((sys.argv[1]=='--u')or(sys.argv[1]=='--U')):
            print("Use the scriipt as :")
            print("Use cmd to give the input")    
        else :
            #Fucntion Call
            DeleteDupliacte(sys.argv[1])


if __name__ == "__main__":
    main()