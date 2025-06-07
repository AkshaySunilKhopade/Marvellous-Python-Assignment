class Calculator:
    
    
    def __init__(self):
        self.value1 = 0
        self.value2=0
        
    def Accept(self):
        print("Enter the radius of Circle:")
        value1 = float(input())
        value2 = float(input())    

    def Addition(self):
        return self.value1+self.value2
       
    def Subtracton(self):
        return self.value1-self.value2

    def Multiplication(self):
        return self.value1*self.value2

    def Division(self):
        return self.value1/self.value2



def main():
    print("Object Oriented Programming")

    A1 = Calculator()
    A1.Accept()
    sum = A1.Addition()
    sub = A1.Subtracton()
    mul = A1.Multiplication()
    div =A1.Division()
    
    print("Addition is :",sum)
    print("Subtraction is :",sub)
    print("Multipliction is :",mul)
    print("Division is :",div)
if __name__ == "__main__":
    main()