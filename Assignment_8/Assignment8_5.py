import threading


def Digits():
    print("From 1 to 50")
    for i in range(1,50+1):
        print(i)


def RevDigits():
    print("From 50 to 1")
    for i in range(50,0,-1):
        print(i)


    
def main():
    
    Thread1 = threading.Thread(target=Digits)
    Thread2 = threading.Thread(target=RevDigits)
    
    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()


if __name__ == "__main__":
    main()