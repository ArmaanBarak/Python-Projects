# imports
import commands
from time import sleep

# default text for dashboard page
def dashboard_text():

    '''
    This is dashboard text, to be displayed every time user reaches homepage
    '''

    print('''\n\nNo Task is being performed right now!

Currently at: Dashboard

Task available:

[0]. View Profile
[1]. Log out
[2]. View list of commands
[3]. Power Off
[4]. Learn More about me
[5]. Learn More about my creator

Enter the respective number below
\n\n''')


# default conditional for dashboard page
def dashboard_conditional(res, page):

    '''
    This function runs control flow for dashboard

    res -> user response for dashboard_text
    page -> current page
    '''

    # default value for logged in 
    logged_in = True


    # control flow
    if res == 0:  # view profile
        print('\nFeature under development\n')
        page = 'Dashboard'

    elif res == 1:  # log out of account
        print('\nLogging you out...\n')
        print('System is performing a task.\n')
        page = 'Homepage'
        logged_in = False

    elif res == 2:  # show list of commands
        print('Showing list of commands!')
        print('System is performing a task.\n')
        commands.show_commands()
        print('\nTask Finished!\n')

    elif res == 3:  # log out and power off
        print('\nLogging you out...\n')
        print('System is performing a task.\n')
        print('Shutting down...\n')
        print('See you soon!')
        sleep(3)
        quit()

    elif res == 4:  # Learn more about OS
        print('\nSorry but my owner is still working on that section.\n')

    else:  # Learn more about owner
        print('\nSorry but my owner is still working on that section.\n')


    # returning current page and if logged in or not
    return page, logged_in
