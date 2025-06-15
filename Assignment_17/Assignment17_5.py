import os
import schedule
import time 
import datetime

def Display():
    filename = "MarvellousLog.txt"
    
    flag = os.path.isabs(filename)
    
    if(flag==False):
        filename = os.path.abspath(filename)
    
    ret = os.path.exists(filename)
    
    if(ret == False):
        fobj.open(filename,"x")
    
    ctime = str(datetime.datetime.now())    
    fobj = open(filename,"a")
    fobj.write(ctime+"\n")
    
def main():
    
    schedule.every(5).seconds.do(Display,)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)    
        
if __name__ == "__main__":
    main()        