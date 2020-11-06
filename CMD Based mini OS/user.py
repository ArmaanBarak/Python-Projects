'''
File with functions necessary for user account
'''

# imports
from time import sleep
from getpass import getpass
import json

# initializing file
def initialize_accounts_file():

    fields = {'Usernames': [], 'Passwords': []}

    with open('accounts.json', 'w') as accounts:

        json.dump(fields, accounts)

# create account function
def create_account():

    '''
    Function to create account
    '''

    print("Fill in the credentials below: \n")

    # Looping to get correct input from user
    while True:

        # user input
        user = input('Username: \n> ')
        pwd = getpass('Password: \n> ')

        with open('accounts.json') as file:
            
            # loading current dictionary with usernames and passwords
            current_dict = json.load(file)

            # If username already exists
            if user in current_dict['Usernames']:
                print("\nThis username already exists, Try Again.\n")
                continue
        
        # adding username and password to dictionary
        current_dict['Usernames'].append(user)
        current_dict['Passwords'].append(pwd)

        # updating file
        with open('accounts.json', 'w') as file:

            json.dump(current_dict, file)

        # Additional functinality
        print('\nCreating account ...\n')
        sleep(2)
        print('Account created successfully!')
        break


initialize_accounts_file()
create_account()
