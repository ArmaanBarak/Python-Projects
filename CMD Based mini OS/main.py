import user

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

print("\n\nWelcome to ARMAAN BARAK's Mini OS!\n\n")

print('''\n
This is a command line based operating system.
You can do a lot here.

This OS is currently under-development but soon it will be turned into a well functioning OS.
After the development period I always be releasing updates for this OS.

The Name hasn't been decided yet but you can give me your suggestions on my github acc or comment below.

There are a lot of commands available right now and you can surely see a list of them anytime you like,
but not while tasks are being performed like, creation or deletion of account, web search,
listening to music, alarms, etc. You can see the list of commands whenever the OS is ready to perform the next task.

I hope you like it here.

* Default id and password is set to admin. You can create your own account too, but unfortunately the accounts file
is reset everytime it's run again so you'll lose them (I'll fix this issue very soon).

** To report bug or give feedback, contact on github or mail me on: armaanbarak@outlook.com\n\n\n
''')

input('Press any key to continue: ')

# initializing accounts file
user.initialize_accounts_file()