import os
import hashlib
import sys
import time



def CheckSum(filepath):
    
        fobj = open(filepath, "rb")
        hobj = hashlib.md5()
        BLOCKSIZE = 1024
        buffer = fobj.read(BLOCKSIZE)

        while len(buffer) > 0:
            hobj.update(buffer)
            buffer = fobj.read(BLOCKSIZE)

        fobj.close()
        return hobj.hexdigest()


def DisplayChecksums(dirname):
    
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
            
    print("Absolute path is : "+DirName)
    FileName = dict
    for FolderName,SubFolder,Files in os.walk(DirName):
        
            for filename in Files :
                filename = FolderName+"/"+filename
                checksum = CheckSum(filename)
                FileName[filename] = checksum
    
    Border = "-"*54
    timestamp = time.ctime()
    #print(timestamp)
    

    filename = "MarvellousLog_%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    #print(filename)
    
    fobj = open(filename,"w")
    fobj.write(Border+"\n")
    fobj.write(FileName)

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

        else:
            #logic            
            DisplayChecksums(sys.argv[1])
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
