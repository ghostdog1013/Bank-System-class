
class Customers:
    def __init__(self, id_number):
        self.id_number = id_number

    def SetUserFirstName(self,first_name):
        self.first_name = first_name

    def SetUserLastName(self,last_name):
        self.last_name = last_name

    def SetUserAddress(self,address):
        self.address = address

    def getUserFirstName():
        return self.first_name

    def getUserLastName():
        return self.last_name

    def getUserAddress(self,address):
        return self.address

    def getUserId(self):
        return self.id_number
