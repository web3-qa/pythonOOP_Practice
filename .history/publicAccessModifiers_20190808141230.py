class BankAcct:
    def __init__(self, initBalance):
        self.init_Balance = initBalance
    
    def getBalance(self):
        return self.getBalance
def main():

    acct = BankAcct(500)

    print('current',acct.getBalance())
    acct.balance += 342524352345
    print('new', acct.balance + acct) 
main()