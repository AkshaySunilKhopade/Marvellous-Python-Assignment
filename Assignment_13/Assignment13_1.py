
class BookStore:
    
    NoOfBooks = 0
    
    def __init__(self,bname,bauthor):
        self.name = bname
        self.author = bauthor
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        
        print("Book name is  ",self.name)
        print("Book author is ",self.author)
        print("No of books of",self.name," are :",BookStore.NoOfBooks)

def main():
    
    Bobj1 = BookStore("Linux System Programming","Robert Love")
    Bobj1.Display()
    
    Bobj2 = BookStore("C Programming ","Dennis Ritchie")
    Bobj2.Display()

if __name__ == "__main__":
    main()