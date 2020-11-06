# imports
from getpass import getpass
import commands
import homepage
import dashboard
import main_functions


# Welcome message 2
print('''
                 ____________    
|          |    |                \\         /   |
|          |    |                 \\       /    |
|          |    |                  \\     /     |
|          |    |                   \\   /      |
|----------|    |--------            \\ /       |
|          |    |                     /        |
|          |    |                    /         |
|          |    |                   /          |
|          |    |____________      /           .
''')

# Welcome message 2
print("\n\nWelcome to ARMAAN BARAK's Mini OS!\n\n")


# Introductory text
print('''\n
This is a command line based operating system.
You can do a lot here.

This OS is currently under-development but soon it will be turned into a well functioning OS.
After the development period I always be releasing updates for this OS.

The Name hasn't been decided yet but you can give me your suggestions on my github acc or comment below.

There are a lot of commands available right now and you can surely see a list of them anytime you like,
but not while tasks are being performed like, creation or deletion of account, web search,
listening to music, alarms, etc. (Don't worry, you'll be informed when a task is in progress)
You can see the list of commands whenever the OS is ready to perform the next task.

To view a full list of commands, type commands and hit enter when the OS is not performing a task.

I hope you like it here.

* Default id and password is set to admin. You can create your own account too, but unfortunately the accounts file
is reset everytime it's run again so you'll lose them (I'll fix this issue very soon).

** To report bug or give feedback, contact on github or mail me on: armaanbarak@outlook.com\n\n\n
''')


input('Press any key to continue: ')

# initializing accounts file
user.initialize_accounts_file()

page = 'Homepage'

# Running OS
while True:

    # if page is homepage
    if page == 'Homepage':
        # printing home page text
        homepage.homepage_text()

        # processing homepage input
        while True:

            # storing returned values
            break_continue, page, logged_in = main_functions.try_except_execute(homepage.homepage_conditional, [0, 1, 2, 3, 4, 5, 6], page)

            # processing program based on returned values
            if break_continue == 'continue':
                continue
            break
    
    # if page is dashboard and user is logged in
    if logged_in:
        
        # displaying dashboard text
        dashboard.dashboard_text()

        # processing homepage input
        while True:

            # storing returned values
            break_continue, page, logged_in = main_functions.try_except_execute(dashboard.dashboard_conditional, [0, 1, 2, 3, 4, 5], page)

            # processing program based on returned values
            if break_continue == 'continue':
                continue
            break
    
    # continuing loop if the OS is not turned off!
    continue
