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
    def getName (self):
        return self.firstName +" "+ self.lastName
    
    def setName (self,xFName, xLName):    
        self.firstName = xFName
        self.lastName = xLName
    def operation03 (self):
        pass
def main():
    emp01 = Employee()
    emp02 = Employee()
    emp03 = Employee()

    print("\t"+"*"*10+ "Welcome to the emp DB" +"*"*10)
    print('First name:', Employee.empCount)
    print('First name:', Employee.payRate)

main()