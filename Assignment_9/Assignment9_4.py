import os
import time
import multiprocessing
import threading

def Fun():
    sum = 0
    for i in range(1,10+1):
        sum = sum + i
    print("Sum is :",sum)

def main():

    T1 = threading.Thread(target=Fun)
    P1 = multiprocessing.Process(target=Fun)
    
    start_F = time.time()
    Fun()
    end_F = time.time()

    start_T = time.time()
    T1.start()
    T1.join()
    end_T = time.time()
    
    start_P = time.time()
    P1.start()
    P1.join()   
    end_P = time.time()
    
    print("Method = ",end_F - start_F)
    print("Thread = ",end_T - start_T)
    print("Process = ",end_P - start_P)

if __name__ == "__main__":
    main()