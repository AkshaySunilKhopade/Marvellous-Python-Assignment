import os


def main():
    
    print("Enter the file name :")
    FileName = input()
    
    #ret = os.path.exists(FileName)
    try :
        fd = open(FileName,"r")
        data = fd.read()
        print("File Data is :")
        print(data)
    except FileExistsError as eobj:
        print(eobj)



if __name__ == "__main__":
    main()