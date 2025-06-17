import shutil
import sys
import time
import os
import schedule


def Traversal(DirSrc,DirDest,Extension):
    
    flag = os.path.isabs(DirSrc)
    if(flag==False):
        DirName = os.path.abspath(DirSrc)
        
    ret = os.path.exists(DirSrc)
    
            
    if(ret==False):
        print("The Path is invalid ")
        exit()
        
    flag = os.path.isdir(DirSrc)
    if(flag==False):
        print("PAth is valid but the target is not directory")
        exit()

    flag = os.path.isabs(DirDest)
    if(flag==False):
        DirBackup = os.path.abspath(DirDest)
    
    ret = os.path.exists(DirDest)   
    if(ret == False):
        os.mkdir(DirBackup)
    
    # print("Absolute path is : "+DirName)

    for FolderName,SubFolder,Files in os.walk(DirSrc):
        
        for filename in Files :
            # filename = FolderName+"/"+filename
            # filename = os.path.join(FolderName,filename)
            if(filename.endswith(Extension)):
                shutil.copy(filename,DirDest)

                
                                    

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

    elif((len(sys.argv))==4):
        #logic
        Traversal(sys.argv[1],sys.argv[2],sys.argv[3])
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
