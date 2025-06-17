import os
import schedule
import time 
import shutil
import datetime
import sys

def Display(Dirname):
    
    Dir = "."
    
    flag = os.path.isabs(Dir)
    
    if(flag==False):
        Dir = os.path.abspath(Dir)
    # print(Dir)
    ret = os.path.isdir(Dir)   
    
    if(ret == False):
        print("Directory Not found")
        exit()
    
    DirBackup = Dirname
    
    flag = os.path.isabs(DirBackup)
    if(flag==False):
        DirBackup = os.path.abspath(DirBackup)
    
    ret = os.path.isdir(DirBackup)   
    if(ret == False):
        os.mkdir(DirBackup)
    
    
    for Folder,SubFolders,Files in os.walk(Dir):
        for filename in Files:
            # filename = os.path.join(SubFolders,filename)
            shutil.copy(filename,DirBackup)
    
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
            Display(sys.argv[1])
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