import Library as lib
import send_email
import datetime
import sys
import schedule
import time

def Index(Dirname,Email,starttime):
    filename,Count,deleted = lib.CreateLog(Dirname)
    send_email.Send_Email(filename,Email,Count,deleted,starttime)

def main():
    start_time = datetime.datetime.now()
    if((len(sys.argv))==2):
        if((sys.argv[1]=='--h') or (sys.argv[1]=='--H')):
            #Heading(Program Desc)
            print("Above Application is used to Find the duplicate values and delete them")
        
        elif((sys.argv[1]=='--u')or(sys.argv[1]=='--U')):
            print("Use the scriipt as :")
            print("Use cmd to give the input")    

    elif((len(sys.argv))==4) :
        #Fucntion Call
        schedule.every(int(sys.argv[2]),).minutes.do(Index,sys.argv[1],sys.argv[3],start_time)
        
        while(True):
            schedule.run_pending()   
            time.sleep(1)
    
    else:
        print("Give 4 Command Line arguements")

if __name__ == "__main__":
    main()