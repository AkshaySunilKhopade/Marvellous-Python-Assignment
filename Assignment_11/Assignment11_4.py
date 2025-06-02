
pow  = 1
def Display(no,counter):
    global pow
    if(counter!=0):
        pow = pow * no
        counter = counter - 1
        Display(no,counter)
        
def main():
    
    value = int(input("Enter the value : "))
    counter = int(input("Enter the counter :"))
    Display(value,counter)
    print(pow)
if __name__ == "__main__":
    main()