import os
import schedule
import datetime 
import time

def Display():
    print(datetime.datetime.now())
def main():
    
    schedule.every(2).seconds.do(Display,)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)    
        
if __name__ == "__main__":
    main()        