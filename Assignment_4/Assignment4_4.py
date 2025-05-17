from functools import reduce 

def Accept(iSize):
    data = list()
    print("Enter the values :")
    for i in range(0,iSize):
        no = int(input())
        data.append(no)
    return data

ChkEven = lambda iNo : (iNo % 2 == 0)

Square = lambda iNo : iNo**2

Add = lambda A,B : A+B  

def main():

    print("Enter the Size  :")
    iNo1 = int(input())

    data = Accept(iNo1)

    fdata = list(filter(ChkEven,data))
    #print(fdata)
    mdata = list(map(Square,fdata))
    #print(mdata)
    rdata = reduce(Add,mdata)
    print(rdata)
if __name__ == "__main__":
    main()