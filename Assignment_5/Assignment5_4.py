
def Max(a,b,c):
    
    if(a>b):
        return a
    elif(b>c):
        return b
    else :
        return c    
    
        
def main():
    
    print("Enterr the first no :")
    a = int(input())
    
    print("Enterr the second no :")
    b = int(input())
    
    print("Enterr the third no :")
    c = int(input())
    

    
    bret = Max(a,b,c)
    print("Largest no is :",bret)
    
if __name__ =="__main__":
    main()