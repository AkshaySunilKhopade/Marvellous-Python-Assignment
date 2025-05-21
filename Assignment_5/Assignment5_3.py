
def VotingEligibility(age):
    bool = False
    if(age >= 18):
        return True

def main():
    
    print("Enterr the Age :")
    age = int(input())
    
    if age < 0 :
        print("please enter correct age")
        return
    
    bret = VotingEligibility(age)
    if(bret):
        print("Eligible to vote")
    else : 
        print("Not Eligible to vote")

if __name__ =="__main__":
    main()