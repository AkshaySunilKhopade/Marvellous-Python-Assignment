
sum  = 0
def Display(no):
    global sum
    if(no!=0):
        digit = int(no % 10)
        print(digit)
        sum = sum + digit
        no = int(no / 10)
        Display(no)
        
def main():
    
    value = int(input("Enter the value : "))
    Display(value)
    print(sum)
if __name__ == "__main__":
    main()