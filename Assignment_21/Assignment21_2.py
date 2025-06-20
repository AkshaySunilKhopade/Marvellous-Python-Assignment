import sys
import psutil
import os 


def ProcessInfo(name):
    List = list()
    try :
        for proc in psutil.process_iter():
            info = proc.as_dict(attrs = ['pid', 'ppid', 'name',  'status', 'username', 'create_time', 'cpu_times', 'cpu_percent', 'memory_info', ])
            if(info['name']==name):
                List.append(info)
            
    except Exception as eobj:
        print(eobj)
    return List

            
def main():
    if((len(sys.argv))==2):
        data = ProcessInfo(sys.argv[1])
        print("Process Details are :")
        for i in data:
          print(i)
          print("\n")  
    else :
        print("Please enter Command Line arugement")


if __name__ == "__main__":
    main()