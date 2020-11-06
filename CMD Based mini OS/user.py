'''
File with functions necessary for user account
'''

# imports
from time import sleep
from getpass import getpass
import json

# initializing file
def initialize_accounts_file():

    fields = {'Usernames': ['admin'], 'Passwords': ['admin']}

    with open('accounts.json', 'w') as accounts:

        json.dump(fields, accounts)


# log in function
def login(user, pwd):

    with open('accounts.json') as accounts:
        
        accounts_dict = json.load(accounts)

        # if username exist in file
        if user in accounts_dict['Usernames']:

            user_idx = accounts_dict['Usernames'].index(user)

            # if password matches with actual password
            if pwd == accounts_dict['Passwords'][user_idx]:
                print('Login Successful!\nAccess Granted!\n\n')
                return True
        
        # if password or username failed to match
        else:
            print('Username or Password didn\'t match!\n\n')
            return False
        

# create account function
def create_account():

    '''
    Function to create account
    '''

    print("Fill in the credentials below: \n")

    print('Extra spaces infront and at end of username and password will be automatically remove off!\nBe careful for lower and uppercases!\n')

    # Looping to get correct input from user
    while True:

        # user input
        user = input('Username: \n$ ').strip()

        # confirming passwords
        while True:

            pwd = getpass('Password: \n$ ')
            confirm = getpass('Confirm Password: \n$ ')

            # is passwords do not match
            if confirm != pwd:
                print("Passwords do not match, Try Again.\n")
                continue

            break
        
        # opening file to confirm username doesn't already exists
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
        print('Account created successfully!\n')
        break


# deleting account
def delete_account():

    # getting desired account to delete
    print('Account deletion in progress.\nFill in the credentials below\n')

    while True:

        user = input('Username: \n$ ').strip()

        # opening accounts file
        with open('accounts.json') as file:
                    
            # loading current dictionary with usernames and passwords
            current_dict = json.load(file)

            # If username doesn't exists
            if user not in current_dict['Usernames']:

                sleep(1)
                print("\nThis username does not exists, Try Again.\n")
                continue

            # getting saved account password
            pwd_idx = current_dict['Usernames'].index(user)
            account_pwd = current_dict['Passwords'][pwd_idx]

        # nested loop for pass confirmation
        while True:

            # getting pass from user
            pwd = getpass('Password: \n$ ')

            # passwords don't match
            if pwd != account_pwd:

                sleep(1)
                print('Passwords do not match.\nAccess Denied!\nTry Again\n')
                sleep(1)
                continue

            # another nested loop for account deletion confirmation
            while True:
                
                # confirming to delete account
                res = input('Are you sure you want to delete the account? Enter (Y or N)\n(Your data would be permanently deleted)\n$ ')

                # If not a valid input
                if res.lower()[0] not in ['y', 'n']:
                    print('Input not recognized!\n')
                    continue
                
                # if sure to delete account
                if res.lower()[0] == 'y':
                    print('DELETION PROCESS CONTINUED!!!\n')
                    sleep(1)
                    break

                # if changed mind
                else:
                    print('Process Terminated!\n')
                    return
            
            # account deletion in progress
            print('Username MATCHED!')
            print('Password MATHCED!')
            print('DELETION IN PROGRESS!\n')
            sleep(2.5)
            break
        
        # updating accounts dictionary
        current_dict['Usernames'].pop(pwd_idx)
        current_dict['Passwords'].pop(pwd_idx)

        # updating file with dictionary
        with open('accounts.json', 'w') as accounts:

            json.dump(current_dict, accounts)
        
        # printing out success message
        print('Your account has been successfully deleted!\n')
        print('Sad to see you go :(\n')
        break                


# test
if __name__ == "__main__":
    
    initialize_accounts_file()
