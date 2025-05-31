import multiprocessing

def Sqaure(data):
    
    for i in range(0,len(data)):
        print(data[i]**2)


def main():
    data = list()
    no = 0
    print("Enter the size ofl list :")
    size = int(input())
    
    print("Enter the elements in list :")
    for i in range(0,size):
        no = int(input())
        data.append(no)

        
    P1 = multiprocessing.Process(target=Sqaure,args=(data,))
    P2 = multiprocessing.Process(target=Sqaure,args=(data,))
    
    P1.start()
    P1.join()

    
    P2.start()
    P2.join()

if __name__ == "__main__":
    main()