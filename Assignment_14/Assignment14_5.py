
class BankAccount:
        
    def __init__(self,):
        self.AccoutNumber = 0
        self.name = ""
        self.Amount = 0
        
    def Accept(self):
        print("Enter the Account no : ")
        self.AccoutNumber = int(input())
        print("Enter the name :")
        self.name = input()
                 
        
    def Depoist(self):
        
        print("Weclome ",self.name)
        print("Enter the amount to deposit :")
        value = int(input())
        self.Amount = self.Amount + value
        print(value,"Amount deposited to your account and aviable balance is :",self.Amount)

    def Withdraw(self):
        print("Weclome ",self.name)
        print("Enter the amount to withdraw :")
        value = int(input())
        if(self.Amount >= value):
            self.Amount = self.Amount - value
            print(value,"Amount debited from your account and aviable balance is :",self.Amount)
        else :
            print("Insufficient Balance")
        
    def Display(self):
        print("Account Number :",self.AccoutNumber)
        print("Account holder :",self.name)
        print("Balnce is :",self.Amount)
        
        
def main():
    
    Acc1 = BankAccount()
    Acc1.Accept()
    Acc1.Depoist()
    Acc1.Withdraw()
    Acc1.Display()
    Acc1.CalInterest() 
    
if __name__ == "__main__":
    main()