

def Addition(iNo1,iNo2):
    return iNo1+iNo2

def Difference(iNo1,iNo2):
    return iNo1-iNo2

def Product(iNo1,iNo2):
    return iNo1*iNo2

def Division(iNo1,iNo2):
    return iNo1/iNo2

def main():
    print("Enter the first number :")
    iNo1 = int(input())
    print("Enter the second number :")
    iNo2 = int(input())
    
    sum = Addition(iNo1, iNo2)
    diff = Difference(iNo1, iNo2)
    product = Product(iNo1, iNo2)
    div = Difference(iNo1, iNo2)
    
    print("Addition is :",sum)
    print("Differnce is :",diff)
    print("Product is :",product)
    print("Division is :",div)

if __name__ == "__main__":
    main()