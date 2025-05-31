import threading 


def EvenNum():
    iCnt = 10*2
    for i in range(1,iCnt+1):
        if((i%2)==0):
            print(i,end=" ")

def OddNum():
    iCnt = 10*2
    for i in range(1,iCnt+1):
        if((i%2)!=0):
            print(i,end=" ")



def main():
    Even = threading.Thread(target=EvenNum)
    Odd = threading.Thread(target=OddNum)
    
    Even.start()
    Even.join()
    
    Odd.start()
    Odd.join()


if __name__ == "__main__":
    main()