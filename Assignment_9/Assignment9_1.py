import threading
import time

def Print():
    for i in range(1,5+1):
        print(i)
        time.sleep(1)


def main():
    
    Thread1 = threading.Thread(target=Print)
    Thread2 = threading.Thread(target=Print)
    Thread3 = threading.Thread(target=Print)
    
    Thread1.start()
    Thread1.join()
    
    Thread2.start()
    Thread2.join()
    
    Thread3.start()
    Thread3.join()
    

if __name__ == "__main__":
    main()