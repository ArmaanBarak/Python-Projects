# imports
import user
import commands
from getpass import getpass
from time import sleep

# default text for homepage 
def homepage_text():

    '''
    This is homepage text, to be displayed every time user reaches homepage
    '''
    
    print('''\n\nNo task is being performed right now!

Currently at: Homepage

Tasks avaialble:
[0]. Learn more about me!
[1]. Login to existing account
[2]. Create Account
[3]. Delete Account
[4]. View list of commands
[5]. Power Off
[6]. Know about my creator!

Enter the respective number below
\n\n''')

# default conditional for homepage
def homepage_conditional(res, page):

    '''
    This function runs control flow for homepage

    res -> user response for homepage_text
    page -> current page
    '''

    # default value for if log in was success or not
    success = False

    # control flow
    if res == 0: # Learn more about the OS
        print('\nSorry but my owner is still working on that section.\n')

    elif res == 1: # Initiate login attempt
        print('Initiating Login attempt for you.')
        print('System is performing a task.\n')

        # getting credentials
        userid = input('Enter username: \n$ ')
        pwd = getpass('Enter password: \n$ ')

        # attempting login
        success = user.login(userid, pwd)

        # processing if log in success or not
        if success:

            print('\nYou are being navigated to dashboard!\n')
            # if log in then page set to dashboard
            page = 'Dashboard'

        else: # If still at homepage
            print('\nYou are still on homepage!\n')
            

    elif res == 2:  # Create user's personal account

        print('Initiating account creation process!')
        print('System is performing a task.\n')

        # creating account
        user.create_account()
        sleep(1)
        print('\nTask Finished!\n')

    elif res == 3:  # Delete user's account
        print('Initiating account deletion process!')
        print('System is performing a task.\n')

        # deleting account
        user.delete_account()
        sleep(1)
        print('\nTask Finished!\n')

    elif res == 4:  # display commands
        print('Showing list of commands!')
        print('System is performing a task.\n')

        # displaying valid commands
        commands.show_commands()
        sleep(1)
        print('\nTask Finished!\n')
    
    elif res == 5:  # Power off OS

        print('Shutting down...\n')
        print('See you soon!')

        sleep(3)
        quit()
    
    else: # Learn more about owner
        print('\nSorry but my owner is still working on that section.\n')
    
    # returning necessary values
    return page, success