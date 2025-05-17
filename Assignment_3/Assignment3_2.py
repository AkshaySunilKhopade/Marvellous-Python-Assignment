
def Maximum(data):
    iMax = 0

    if(len(data)==0):
        return 0
    
    for i in range(0,len(data)):
        if(data[i] > iMax):
            iMax = data[i]        

    return iMax

def main():
    
    print("Enter the size :")
    iSize = int(input())

    data = list()
    
    for i in range(0,iSize):
        value = int(input())
        data.append(value)
    
    iRet = Maximum(data)
    print(iRet)

if __name__ == "__main__":
    main()