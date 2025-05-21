
def Vowel(char):
    bRet = False
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        bRet = True
    return bRet
               
    


def main():
    print("Enter the one character :")
    cstr = input()
    char = ''
    if(len(cstr)==1):
        char = cstr
    else :
        print("Enter only one Characte")
        return

    ret = Vowel(char)
    
    if(ret):
        print("It is Vowel")
    else :
        print("It is Consonant")
        
    
    
if __name__ == "__main__":
    main()