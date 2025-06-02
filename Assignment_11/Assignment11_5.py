
zero  = 0
def Display(no):
    global zero
    if(no!=0):
        digit = int(no % 10)
        if(digit==0):
            zero = zero + 1
        no = int(no / 10)
        Display(no)
        
def main():
    
    value = int(input("Enter the value : "))
    Display(value)
    print(zero)
if __name__ == "__main__":
    main()