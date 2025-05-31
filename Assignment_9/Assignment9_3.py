import multiprocessing
import time


def Factorial(iNo):
    fact = 1
    for i in range(1,iNo+1):
        fact = fact * i
    return fact


def main():
    data = list()
    no = 0
    print("Enter the size ofl list :")
    size = int(input())
    
    print("Enter the elements in list :")
    for i in range(0,size):
        no = int(input())
        data.append(no)

    P1 = multiprocessing.Pool()
    result = P1.map(Factorial,data)
    
    P1.close()
    P1.join()
    
    print(result)
        

if __name__ == "__main__":
    main()