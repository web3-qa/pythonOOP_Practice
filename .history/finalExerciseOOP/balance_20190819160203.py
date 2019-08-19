class Balance:
    def __init__(self,initial_balance):
        self.__balance = initial_balance
    
    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

    def show_balance(self):
        return self.__balance 

    def transfer(self, transfer_amount):
        if __balance < transfer_amount:
            print ("unable to transfer")
        

class CheckingAcct(Balance):
    
    def __init__(self, inital_balance):
        Balance.__init__(self, inital_balance)
    

class SavingsAcct(Balance):
    
    def __init__(self, inital_balance):
        Balance.__init__(self, inital_balance)