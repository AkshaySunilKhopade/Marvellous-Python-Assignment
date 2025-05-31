import threading 


def EvenNum():
    print("Enter the number :")
    ino = int(input())
    isum = 0
    iCnt = (int)(ino/2)
    for i in range(1,iCnt):
        if((ino%i)==0):
            if((i%2)==0):
                isum = isum + i

    print("Even Factors sum is :",isum)


def OddNum():
    print("Enter the number :")
    ino = int(input())
    isum = 0
    iCnt = (int)(ino/2)
    for i in range(1,iCnt):
        if((ino%i)==0):
            if((i%2)!=0):
                isum = isum + i
                
    print("Odd Factors sum is :",isum)




def main():
    Even = threading.Thread(target=EvenNum)
    Odd = threading.Thread(target=OddNum)
    
    Even.start()
    Even.join()
    
    Odd.start()
    Odd.join()

    print("Exit from main()")
if __name__ == "__main__":
    main()