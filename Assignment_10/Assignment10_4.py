from functools import reduce


ChkNum = lambda no : (no%2==0)

Increase = lambda no : no**2

Sum = lambda A,B : A+B



def Accept(size):
    data = list()
    print("Entr the elements :")
    for i in range(0,size):
        no = int(input())
        data.append(no)
    return data


def main():
    print("Enter the size :")
    size = int(input())
    
    data = list()
    
    data = Accept(size)
    
    fdata = list(filter(ChkNum,data))
    mdata = list(map(Increase,fdata))
    ret = reduce(Sum,mdata)
    print()

if __name__ == "__main__":
    main()