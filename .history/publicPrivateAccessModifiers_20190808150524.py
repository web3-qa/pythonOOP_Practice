class Cust:
    def __init__(self, fName, lName):
        self.__firstName =  fName
        self.__lastName = lName
    def getName():
        return _Cust__firstName, _Cust__lastName

class BankAcct:
    def __init__(self, initBalance):
        self.__balance = initBalance
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amountDep):
        self.__balance += amountDep
    def __del__(self):
        pass

def main():
    
    acct = BankAcct(500)
    acct.deposit(500)

    # print('current',acct.balance())
    print() 
    del(acct)
    print('aaaa', acct.getBalance()) 

main()