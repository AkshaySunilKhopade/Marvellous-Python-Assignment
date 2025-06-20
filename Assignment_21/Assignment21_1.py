import os
import psutil

def ProcessInfo():
    
    print("--------------------------Process Information------------------------------")
    fobj = open("Marvellous.txt","w")
    try:
        for Process in psutil.process_iter():
            info = Process.as_dict(attrs=['pid','name'])
            print(info)
            fobj.write(str(info))
            fobj.write("\n")
    except Exception as eobj:
        print(eobj)
    
   
    
def main():
    ProcessInfo()

if __name__ == "__main__":
    main()