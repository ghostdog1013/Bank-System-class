#!/usr/bin/env python
from random import randint
import logging as log
import Services
import BankAccount
import Customer
import Employee


mylogs = logging.getLogger(__name__)
mylogs.setLevel(logging.DEBUG)
file = logging.FileHandler('banking.log')
file.setLevel(logging.INFO)
fileformat = logging.Formatter(
    "%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S")
file.setFormatter(fileformat)
mylogs.addHandler(file)
db_logger = logging.getLogger('sqlalchemy')
db_logger.addHandler(file)
db_logger.setLevel(logging.INFO)



if __name__ == '__main__':

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = first_name + last_name
    address = input("Enter address: ")

    person_type = int(input("Are you a Customer or an Employee?\n"
                            "Enter 1 for 'Customer'\n"
                            "Enter 2 for 'Employee'\n"))

    if person_type == 1:

        person = Customer(first_name, last_name, address, 0)
        cash_input = input("Currently, you have no cash available.\n"
                           "Enter 'Y' if this is the case.\n"
                           "Otherwise, enter new cash amount: ")
        if cash_input != 'Y':
            person.set_cash_available(cash_input)
    elif person_type == 2:

        cash_input = input("Currently, you have no cash available.\n"
                           "Enter 'Y' if this is the case.\n"
                           "Otherwise, enter new cash amount: ")
        salary_input = int(input("Enter current salary: "))

        person = Employee(first_name, last_name, address, cash_input, salary_input)
        if cash_input != 'Y':
            cash_input = int(cash_input)
            person.set_cash_available(cash_input)

        employee_req = int(input("Enter 1 to increase salary\n"
                                 "Enter 2 to request employee data from JSON (if exists)\n"
                                 "Enter 3 to perform no action: "))
        if employee_req == 1:
            person.increase_salary()
            person.employee_to_json()  # Save file in JSON format
        elif employee_req == 2:
            try:
                person.employee_from_json()  # May need try/except clause
            except ValueError:
                print("No JSON file found.")
        elif employee_req == 3:
            print("Did not perform action.")


    visit_bank_req = input("Would you like to visit the bank?\n"
                           "Enter 'Y' for Yes and 'N' for No: ")
    if visit_bank_req == 'Y':
        active_person = person.visit_bank()
        print("Person has chosen to visit the bank!")

        action_req = int(input("Enter number for specified action:\n"
                               "Enter 1 to withdraw\n"
                               "Enter 2 to deposit\n"
                               "Enter 3 to display current balance: "))
        if action_req == 1:
            active_person.withdraw()
        elif action_req == 2:
            active_person.deposit()
        elif action_req == 3:
            active_person.display()

        more_action_req = input("Would you like to perform another action?\n"
                                "Enter 'Y' for another action and "
                                "'N' to stop using the banking system: ")
        while more_action_req == 'Y':

            action_req2 = int(input("Enter number for specified action:\n"
                                    "Enter 1 to withdraw\n"
                                    "Enter 2 to deposit\n"
                                    "Enter 3 to display balance\n"
                                    "Enter 4 to use a service: "))
            if action_req2 == 1:
                active_person.withdraw()
            elif action_req2 == 2:
                active_person.deposit()
            elif action_req2 == 3:
                active_person.display()

    elif visit_bank_req == 'N':
        print("Did not visit bank.\n"
              "You will not be able to use any services without first visiting the bank "
              "and performing an action.")
