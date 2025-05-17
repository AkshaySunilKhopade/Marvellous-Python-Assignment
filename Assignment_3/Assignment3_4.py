
def RepeadetDigit(data,iNo):
    iCnt = 0

    if(len(data)==0):
        return 0
    
    for i in range(0,len(data)):
        if(data[i]==iNo):
            iCnt += 1             

    return iCnt

def main():
    
    print("Enter the size :")
    iSize = int(input())

    print("Enter the value :")
    iNo = int(input())

    data = list()
    
    print("Enter the elements in List :")
    for i in range(0,iSize):
        value = int(input())
        data.append(value)
    
    iRet = RepeadetDigit(data,iNo)
    print(iRet)

if __name__ == "__main__":
    main()