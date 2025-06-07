
class BankAccount:
    
    ROI = 10.5
    
    def __init__(self,aname):
        self.name = aname
        self.Amount = 0
        
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
    
    def CalInterest(self):
          SI = self.Amount*BankAccount.ROI*1
          print("Interest for 1 year is :",SI) 
    
    def Display(self):
        print("Account holder :",self.name)
        print("Balnce is :",self.Amount)
        
        
def main():
    
    Acc1 = BankAccount("Akshay")
    Acc1.Depoist()
    Acc1.Withdraw()
    Acc1.Display()
    Acc1.CalInterest() 
    
if __name__ == "__main__":
    main()