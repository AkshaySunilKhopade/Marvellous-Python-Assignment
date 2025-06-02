ino = 1
    
def Display(no):
    global ino
    if(no>=1):
        #while(no>=1)
        
        print(ino,end=" ")
        ino = ino + 1
        no = no - 1
        Display(no)

def main():
    
    value = int(input("Enter the value : "))
    Display(value)

if __name__ == "__main__":
    main()