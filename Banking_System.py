#!/usr/bin/env python
from random import randint
import logging as log

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
