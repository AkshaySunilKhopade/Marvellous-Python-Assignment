
class Vehicle:
    def __init__(self,str):
        self.Name = str

    def start(self):
        print("Name : ",self.Name)
        print("Start mthod of Vehicle Class")

class Car(Vehicle):
    
    def __init__(self,str):
        super().__init__(str)
                
    def start(self):
        print("Name : ",self.Name)
        print("Start mthod of CAR Class")

        
def main():

    Car1 = Car("AKshay")
    Car1.start()
    

if __name__ == "__main__":
    main()