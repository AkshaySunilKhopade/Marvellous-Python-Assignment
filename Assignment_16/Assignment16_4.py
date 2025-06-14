import os


def Calculate(Filename):
    flag = os.path.isabs(Filename)
    if(flag==False):
        Filename = os.path.abspath(Filename)
        
    ret = os.path.exists(Filename)
    
    fobj = None    
    if(ret==False):
        fobj = open(Filename,"w")
    no = []
    fobj = open(Filename,"a")
    print("Enter the 10 numbers ")
    for i in range(1,10+1):
        num = int(input())
        no.append(num)
    for i in range(0,len(no)):
        fobj.write(str(no[i])+'\n')
    
    
def main():
    print("enter the file name: ")
    FileName = input()
    
    Calculate(FileName)

if __name__ == "__main__":
    main()