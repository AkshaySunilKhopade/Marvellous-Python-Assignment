
def Conveter(Celsius):
    Fah = (Celsius * 9/5)+32
    return Fah




def main():
    
    print("Enter tempreature in Celisus :")
    Celsius = float(input())
    
    Fah = Conveter(Celsius)
    print("Temperature in Fahrenheit :",Fah,"°F")    


if __name__ == "__main__":
    main()