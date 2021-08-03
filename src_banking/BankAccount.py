
class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
        self.SavingAccount = {}
        self.CheckingAccount = {}
        self.accountNumber = randint(10000,99999)

    def create_new_acc(self,name,account_type,deposit):
        # assert(deposit > 0)

        self.account_type =  account_type
        if account_type == 'checking':
            self.CheckingAccount[self.accountNumber] = [name, deposit]
        elif account_type == 'saving':
            self.SavingAccount[self.accountNumber] = [name, deposit]
        else:
            log.warning('Invalid account type')

    # specify which account to withdraw?
    def withdraw(self, amount):
        if amount > self.balance:
            log.error('Amount to withdraw cannot exceed current balance')

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            log.error('Amount to deposit cannot be negative')

        self.balance += amount
        return self.balance

    def display(self):
         print("\n Net Available Balance=",self.balance)
