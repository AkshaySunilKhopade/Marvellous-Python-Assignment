import threading 


def EvenNum(List):
    
    sum = 0
    
    for i in range(0,len(List)):
        if((List[i]%2)==0):
            sum = sum + List[i]
    print("Sum of even list is :",sum)
    
def OddNum(List):
    
    sum = 0
    
    for i in range(0,len(List)):
        if((List[i]%2)!=0):
            sum = sum + List[i]
    
    print("Sum of odd list is :",sum)
    


def main():
    print("Enter the size :")
    size = int(input())
    print("Enter the elements in list :")
    intput_list = list()
    
    for i in range(0,size):
        ino = int(input())
        intput_list.append(ino)
    
    Even = threading.Thread(target=EvenNum,args=(intput_list,))
    Odd = threading.Thread(target=OddNum,args=(intput_list,))
    
    Even.start()
    Even.join()
    
    Odd.start()
    Odd.join()


if __name__ == "__main__":
    main()