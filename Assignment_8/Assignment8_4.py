import threading

def SmallLetter(str):

    count = 0
    
    for i in str:
        if(i.islower()):
            count += 1
    print("Small Letters are :",count)
    print("thread id is :",threading.get_ident())
    print("thread name is :",threading.current_thread())

def CapitalLetter(str):
    count = 0
    
    for i in str:
        if(i.isupper()):
            count += 1
    print("Capital Letters are :",count)
    print("thread id is :",threading.get_ident())
    print("thread name is :",threading.current_thread())

def Digits(str):

    count = 0
    
    for i in str:
        if(i.isnumeric()):
            count += 1
    print("Digits are :",count)
    print("thread id is :",threading.get_ident())
    print("thread name is :",threading.current_thread())

def main():
    print("Enter the string :")
    str = input()
    
    small = threading.Thread(target = SmallLetter,args=(str,))
    capital = threading.Thread(target=CapitalLetter,args=(str,))
    digit = threading.Thread(target=Digits,args=(str,))
    
    small.start()
    small.join()

    capital.start()
    capital.join()
   
    digit.start()
    digit.join()


if __name__ == "__main__":
    main()