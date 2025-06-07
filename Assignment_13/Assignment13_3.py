
class Number:
    
    
    def __init__(self,value):
        self.no = value

    def ChkPrime(self):
        iRet = True
        counter  = (int)(self.no/2 + 1)

        for i in range(2,counter):
            if(self.no%i==0):
                iRet = False

        return iRet

    def ChkPerfect(self):
        iRet = True
        sum = 0
        counter  = (int)(self.no/2 + 1)

        for i in range(1,counter):
            if(self.no%i==0):
               sum = sum + i 
    
        if(sum==self.no):
            return iRet
        else :
            iRet = False
            return iRet    
    
    def Factors(self):
        counter  = (int)(self.no/2 + 1)
        factors = list()
        
        for i in range(1,counter):
            if(self.no%i==0):
                factors.append(i) 
        return factors
        
    def SumFactors(self):
        facts = self.Factors()
        sum = 0
        for i in range(0,len(facts)):
            sum = sum + facts[i]
        return sum           
    
def main():
    
    print("Enter th number :")
    no = int(input())
    
    Nobj = Number(no)
    Primeno = Nobj.ChkPrime()
    Perfectno = Nobj.ChkPerfect()
    Facts = Nobj.Factors()
    Sum = Nobj.SumFactors()
    
    if(Primeno):
        print("No is prime")
    else :
        print("Number is not prime")
    
    if(Perfectno):
        print("No is perfect")
    else :
        print("Number is not perfect")
    
    print("Facts are :",Facts)
    
    print("Sum of factors is :",Sum)
    
           
if __name__ == "__main__":
    main()