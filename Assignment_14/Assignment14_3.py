
class Book:
    
    def __init__(self,bname):
        self.name = bname
        self.__price = 0

    def set_price(self,value):
        self.__price = value
    def get_price(self):
        return self.__price
    def Display(self):
        print("Book name = ",self.name)
        print("Price = ",self.__price)    
        
def main():

    Bobj = Book("Let us C")
    Bobj.set_price(1000)
    Bobj.Display()
    price = Bobj.get_price()
    print(price)
if __name__ == "__main__":
    main()