class Employee:
    'the base classe for employee'
    #Class variables
    empCount = 0
    payRate = 10

    #This is our initiialiser metho when a new object is created.
    #Class Data Attribute
    def __init__(self):
        self.firstName = 'N/A'
        self.lastName = 'N/A'
        self.uid = 'N/A'


    #Ojbect Data Attributes

    #Methods
    def operation01 (self):
        pass
    
    def operation02 (self):    
        pass

    def operation03 (self):
        pass
def main():
    print("*"*10"Welcome to the emp DB""*")
    print('First name:', Employee.empCount)
    print('First name:', Employee.payRate)

main()