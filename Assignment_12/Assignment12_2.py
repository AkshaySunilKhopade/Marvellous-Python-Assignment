


class Circle:
    
    PI = 3.14
    
    def __init__(self):
        self.radius = 0
        self.Area = 0.0
        self.Circumference = 0.0
        
    def Accept(self):
        print("Enter the radius of Circle:")
        radi = float(input())
        self.radius=radi    

    def CalArea(self):
        self.Area = Circle.PI*(self.radius**2)
        
    def CalCircumference(self):
        self.Circumference = 2*Circle.PI*self.radius
    
    def Display(self):
        print("Radis is :",self.radius)
        print("Area is :",self.Area)
        print("Circumference is :",self.Circumference)

def main():
    print("Object Oriented Programming")

    C1 = Circle()
    C1.Accept()
    C1.CalArea()
    C1.CalCircumference()
    C1.Display()
if __name__ == "__main__":
    main()