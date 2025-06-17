import sys
import time
import os
import schedule


def Traversal(DirName,Extension,ExtensionChange):
    
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
            # filename = os.path.join(FolderName,filename)
            if(filename.endswith(Extension)):
                root,ext = filename.rsplit(".",1)
                newFileName = root+ExtensionChange

                path1 = os.path.join(FolderName,filename)            #error was we wrer using the filename only notthe path we need the whole path to replce
                path2 = os.path.join(FolderName,newFileName)

                os.rename(path1,path2)

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
