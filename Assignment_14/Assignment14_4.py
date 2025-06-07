
class School:
    SchoolName = ""
    def __init__(self):
        self.empname = ""
        self.rollno = 0
        

    def Accept(self):
        name = ""
        id  = 0
        
        print("Enter the  name :")
        name = input()
        print("Enter the ID :")
        id = int(input())
        
        
        self.name = name
        self.rollno = id

    def Display(self):
        print("Name :",self.name)
        print("ID :",self.rollno)
        print("School name is :",School.SchoolName)    
        
def main():

    Eobj = School()
    Eobj.Accept()
    
    School.SchoolName = "MIT"
    Eobj.Display()

    
if __name__ == "__main__":
    main()