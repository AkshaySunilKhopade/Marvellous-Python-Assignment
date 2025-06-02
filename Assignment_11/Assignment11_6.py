ino = 0
    
def Display(no):
    global ino
    if(no>=1):
        #while(no>=1)
        ino = ino + no
        no = no - 1
        Display(no)

def main():
    
    value = int(input("Enter the value : "))
    Display(value)
    print(ino)

if __name__ == "__main__":
    main()