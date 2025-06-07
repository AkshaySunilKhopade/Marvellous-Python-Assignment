
class Person:
    def __init__(self,str,no):
        self.Name = str
        self.Age = no

class Teacher(Person):
    
    def __init__(self,str,age,val):
        super().__init__(str,age)
        self.salary = val           
                
    def Display(self):
        print("Name :",self.Name)
        print("Age :",self.Age)
        print("Salary is :",self.salary)
    
        
def main():

    Teacher1 = Teacher("AKshay",22,10000)
    Teacher1.Display()
    

if __name__ == "__main__":
    main()