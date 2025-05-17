from functools import reduce 

def Accept(iSize):
    data = list()
    print("Enter the values :")
    for i in range(0,iSize):
        no = int(input())
        data.append(no)
    return data

Sort = lambda no : no >= 70 and no <= 90

Increase = lambda ivalue :  ivalue + 10

Product = lambda A,B : A+B 

def main():

    print("Enter the Size  :")
    iNo1 = int(input())

    data = Accept(iNo1)

    fdata = list(filter(Sort,data))
    #print(fdata)
    mdata = list(map(Increase,fdata))
    #print(mdata)
    rdata = reduce(Product,mdata)
    print(rdata)
if __name__ == "__main__":
    main()