
class Reactangle:
    
    def __init__(self):
        self.lenght = 0.0
        self.width = 0.0
         

    def Accept(self):
        no1 = 0.0
        no2 = 0.0

        print("Enter the Length :")
        no1 = float(input())
        
        print("Enter the Breath :")
        no2 = float(input())
        
        self.lenght = no1
        self.width = no2
        
    def CalArea(self):
        return self.lenght*self.width

    def CalPerimeter(self):
        return self.lenght+self.width
    
        
def main():

    Robj = Reactangle()
    Robj.Accept()
    retA = Robj.CalArea()
    retP = Robj.CalPerimeter()
    print("Area = ",retA)
    print("Peritmeter = ",retP)

if __name__ == "__main__":
    main()