

class Services:
    def __init__(self,service_type):
        self.service_type = service_type
        self.loan_account = {}
        self.credit_account = {}
        self.accountNumber = randint(10000,99999)

    def getServiceType(self):
        return self.service_type

    def create_new_service(self,account_type,amount,duration):

        if amount < 0:
            log.error('loan/credit amount cannot be negative')

        self.account_type =  account_type
        if self.account_type == 'loan':
            self.loan_account[self.accountNumber] = [amount, duration]
        elif self.account_type == 'credit':
            self.credit_account[self.accountNumber] = [amount, duration]
        else:
            log.warning('Invalid account type')

    def getCurrentLoanAmount(self):
        return self.loan_account[self.accountNumber][0]

    def getCurrentCreditAmount(self):
        return self.credit_account[self.accountNumber][0]

    def getCurrentLoanDuration(self):
        return self.loan_account[self.accountNumber][1]

    def getCurrentCreditDuration(self):
        return self.credit_account[self.accountNumber][1]
