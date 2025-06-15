import os
import schedule
import time 

def Display():
    print("Jay Ganesh...")
    # filename = "MarvellousLog.txt"
    
    # flag = os.path.isabs(filename)
    
    # if(flag==False):
    #     filename = os.path.abspath(filename)
    
    # ret = os.path.exists(filename)
    
    # if(ret == False):
    #     fobj.open(filename,"x")
    
        
    # fobj = open(filename,"a")
    # fobj.write("Jay Ganesh..."+"\n")
    
def main():
    
    schedule.every(2).seconds.do(Display,)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)    
        
if __name__ == "__main__":
    main()        