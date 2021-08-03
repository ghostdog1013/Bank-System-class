class Employees:
    def __init__(self, id_number):
        self.id_number = id_number

    def SetEmployeesFirstName(self,first_name):
        self.first_name = first_name

    def SetEmployeesLastName(self,last_name):
        self.last_name = last_name

    def SetEmployeesAddress(self,address):
        self.address = address

    def getEmployeesFirstName():
        return self.first_name

    def getEmployeesLastName():
        return self.last_name

    def getEmployeesAddress(self,address):
        return self.address

    def getEmployeesId(self):
        return self.id_number
