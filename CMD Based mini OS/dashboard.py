def dashboard_text():
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

def dashboard_conditional(res, page, userid, pwd):

    if res == 0:
        print('''
username: 
''')