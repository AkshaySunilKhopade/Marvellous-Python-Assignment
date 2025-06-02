
Fact  = 1
def Display(no):
    global Fact
    if(no>=1):
        Fact = Fact * no
        no = no - 1
        Display(no)       
    
def main():
    
    value = int(input("Enter the value : "))
    Display(value)
    print(Fact)
if __name__ == "__main__":
    main()