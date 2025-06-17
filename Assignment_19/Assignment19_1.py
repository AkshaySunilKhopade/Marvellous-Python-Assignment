#Program 


import sys
import time
import os
import schedule


def Traversal(DirName,Extension):
    
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
                print(filename)
                                    

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

    elif((len(sys.argv))==3):
        #logic
        Traversal(sys.argv[1],sys.argv[2])
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
