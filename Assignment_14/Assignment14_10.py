
class Employee:
    
    def __init__(self,name,dept,sal):
        self.empname = name
        self._department = dept
        self.__Salary = sal


    def Display(self):
        print("Name :",self.empname)
        print("DepartMent :",self._department)
        print("Salary is :",self.__Salary)
        
        
def main():

    Eobj = Employee("Akshay","Abc",20000)
    Eobj.Display()

if __name__ == "__main__":
    main()