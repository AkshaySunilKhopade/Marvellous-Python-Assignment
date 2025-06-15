import os
import schedule
import datetime 
import time

def Lunch():
    print("Now its Lunch time.....")
def WrapUp():
    print("Wrap Up .....")
def main():
    
    schedule.every().days.at("13:00").do(Lunch,)
    schedule.every().days.at("18:00").do(WrapUp,)
    
    while(True):
        schedule.run_pending()
        time.sleep(1)    
        
if __name__ == "__main__":
    main()        