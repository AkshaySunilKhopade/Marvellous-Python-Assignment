
class Employee:
    
    def __init__(self):
        self.empname = ""
        self.emp_id = 0
        self.Salary = 0

    def Accept(self):
        name = ""
        id  = 0
        salary = 0
        print("Enter the Employee name :")
        name = input()
        print("Enter the ID :")
        id = int(input())
        print("enter the salary :")
        salary = 0
        
        self.name = name
        self.emp_id = id
        self.Salary = salary

    def Display(self):
        print("Name :",self.name)
        print("ID :",self.emp_id)
        print("Salary is :",self.Salary)
        
        
def main():

    Eobj = Employee()
    Eobj.Accept()
    Eobj.Display()

if __name__ == "__main__":
    main()