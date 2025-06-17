import os 
import sys


def CopyFile(filename):
    
    flag = os.path.isabs(filename)

    if(flag==False):
        filename = os.path.abspath(filename)

    flag = os.path.isdir(filename)
    if(flag==True):
        print("It is Directory")
        exit()
    
    Ret = False
    
    flag = os.path.exists(filename)
    if(flag==False):
        print("File Not Exist")
    
    fobj1 = open("Demo.txt","x")
    fobj2 = open(filename,"r")
    
    for line in fobj2:
        fobj1.write(line)
    
def main():
    Border = "-"*54
    print(Border)
    print("_________________MARVELLOUS AUTOMATION________________")
    print(Border)

    #logic
    
    if((len(sys.argv)==2)):
        if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform-----")
            print("This is the automation script")

        elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
            print("use the given script as ")
            print("ScriptName.py Argument1 Arguement2")
            
        else:
        #logic
            CopyFile(sys.argv[1])
    
    
    else :
        print("Invalid no of arguements")
        print("Use the given flags as :")
        print("--h to display the help")
        print("--u to display the usage")
        
        


    print(Border)
    print("_____________Thank you for using our script___________")
    print("_________________MARVELLOUS INFOSYSTEMS_______________")
    print(Border)
   

if __name__ == "__main__":
    main()
    
