
def EvenOdd(no):
    bool = False
    if((no%2)==0):
        return True

def main():
    
    print("Enterr the No :")
    no = int(input())
    
    bret = EvenOdd(no)
    if(bret):
        print("Even")
    else : 
        print("Odd")

if __name__ =="__main__":
    main()