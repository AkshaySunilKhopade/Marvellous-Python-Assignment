import os
import schedule
import datetime 
import time

def Display():
    print("Namaskar...")
def main():
    
    schedule.every().days.at("09:00").do(Display,)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)    
        
if __name__ == "__main__":
    main()        