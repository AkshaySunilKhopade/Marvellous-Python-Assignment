import os
import schedule
import datetime 
import time

def Display():
    print("Checking Email.....")
def main():
    
    schedule.every(10).seconds.do(Display,)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)    
        
if __name__ == "__main__":
    main()        