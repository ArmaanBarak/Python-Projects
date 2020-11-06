import user
import commands
from getpass import getpass
from time import sleep

def homepage_text():
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

def homepage_conditional(res, page, userid='admin', pwd='admin'):

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

        if success:
            print('\nYou are being navigated to dashboard!\n')

        else:
            print('\nYou are still on homepage!\n')

        page = 'Dashboard'
            

    elif res == 2:  # Create user's personal account
        print('Initiating account creation process!')
        print('System is performing a task.\n')
        user.create_account()
        print('\nTask Finished!\n')

    elif res == 3:  # Delete user's account
        print('Initiating account deletion process!')
        print('System is performing a task.\n')
        user.delete_account()
        print('\nTask Finished!\n')

    elif res == 4:
        print('Showing list of commands!')
        print('System is performing a task.\n')
        commands.show_commands()
        print('\nTask Finished!\n')
    
    elif res == 5:
        print('Shutting down...\n')
        print('See you soon!')
        sleep(3)
        quit()
    
    else:
        print('\nSorry but my owner is still working on that section.\n')
    
    return page