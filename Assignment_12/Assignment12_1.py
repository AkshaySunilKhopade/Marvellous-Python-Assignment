


class Demo:
    
    c_var = 21
    
    def __init__(self,value1,value2):
        self.no1 = value1
        self.no2 = value2
        
    def fun(self):
        print("Inside Fun")
        print("no1 =",self.no1)
        print("no2 =",self.no2)

    def gun(self):
        print("Inside Gun")
        print("no1 =",self.no1)
        print("no2 =",self.no2)


def main():
    print("Object Oriented Programming")

    Obj1=Demo(11,21)
    Obj2 = Demo(51,101)
    
    Obj1.fun()
    Obj1.gun()
    
    Obj2.fun()
    Obj2.gun()
    
    print("Class varible c_var =",Demo.c_var)    

if __name__ == "__main__":
    main()