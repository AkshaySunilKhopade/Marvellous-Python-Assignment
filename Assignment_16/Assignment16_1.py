
def main():
    
    print("Creationg Student.txt")
   
    fd = open("Student.txt","w")
    
    print("Enter the 5 names :")
    data = list()
    
    for i in range(0,5):
        names = input()
        data.append(names)
    
    print(data)
    fd.writelines(data)

    fd.close()
    

if __name__ =="__main__":
    main()