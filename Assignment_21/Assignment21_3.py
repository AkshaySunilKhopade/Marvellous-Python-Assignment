import sys
import psutil
import os 


def CreateLog(Dirname):

    data = ProcessInfo()
    
    flag = os.path.isabs(Dirname)
    if(flag==False):
        Dirname = os.path.abspath(Dirname)
    
    flag = os.path.exists(Dirname)
    if(flag==False):
        os.mkdir(Dirname)

    filename = Dirname+"/Marvellous.txt"
    fobj = open(filename,"w")
    for values in data:
        fobj.write(str(values))
        fobj.write("\n")


def ProcessInfo():
    List = list()
    try :
        for proc in psutil.process_iter():
            info = proc.as_dict(attrs = ['pid', 'ppid', 'name',  'status', 'username'])
            List.append(info)
    except Exception as eobj:
        print(eobj)
    return List

            
def main():
    if((len(sys.argv))==2):
        CreateLog(sys.argv[1])
      
    else :
        print("Please enter Command Line arugement")


if __name__ == "__main__":
    main()