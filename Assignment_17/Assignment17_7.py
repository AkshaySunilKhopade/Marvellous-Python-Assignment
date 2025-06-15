import os
import schedule
import time 
import shutil
import datetime

def Display():
    
    Dir = "."
    
    flag = os.path.isabs(Dir)
    
    if(flag==False):
        Dir = os.path.abspath(Dir)
    # print(Dir)
    ret = os.path.isdir(Dir)   
    
    if(ret == False):
        print("Directory Not found")
        exit()
    
    DirBackup = "backup"
    
    flag = os.path.isabs(DirBackup)
    if(flag==False):
        DirBackup = os.path.abspath(DirBackup)
    
    ret = os.path.isdir(DirBackup)   
    if(ret == False):
        os.mkdir(DirBackup)
    
    filename = "MarvellousLog.txt"
    # print(filename)
    
    ret = os.path.exists(filename)
    
    if(ret==False):
        fobj=open(filename,"x")
    fobj = open(filename,"a")
    
    for Folder,SubFolders,Files in os.walk(Dir):
        for filename in Files:
            ctime = str(datetime.datetime.now())
            # filename = os.path.join(SubFolders,filename)
            fobj.write(filename+" : "+ctime+"\n")
            shutil.copy(filename,DirBackup)
    
def main():
    
    schedule.every(1).hour.do(Display,)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
         
if __name__ == "__main__":
    main()        