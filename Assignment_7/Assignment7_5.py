

def Accept():
    print("Enter the Stirng :")
    data = input()    
    return data    

def Palindrome(str):
    slength = len(str)-1
    revstr = ""
    bool = False
    j = 0
    for i in range(slength,-1,-1):
        revstr= revstr+str[i]
        # print(revstr)
        # print(str[i])
    
    if(str == revstr):
        bool = True       
    return bool 
    
def main():
    str = Accept()
    rstr = Palindrome(str)
    
    if(rstr):
        print("String is palindrome")
    else :
        print("String is not palindrome")
    
        
if __name__ == "__main__":
    main()