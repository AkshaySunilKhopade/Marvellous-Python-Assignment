import Arthimetic



def main():
    print("Enter the first number : ")
    iNo1 = int(input())
    print("Enter the second number : ")
    iNo2 = int(input())

    iSum = Arthimetic.Add(iNo1,iNo2)
    iSub = Arthimetic.Sub(iNo1,iNo2)
    iMul = Arthimetic.Mul(iNo1,iNo2)
    iDiv = Arthimetic.Div(iNo1,iNo2)

    print("Sum is :",iSum)
    print("Subtraction is :",iSub)
    print("Mulitpication  is  :",iMul)
    print("Division is :",Arthimetic.Div(iNo1,iNo2))
if __name__ == "__main__":
    main()