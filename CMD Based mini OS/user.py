from getpass import getpass

def create_account():

    """
    Function to create account
    """

    print("Fill in the credentials below: \n")

    user = input("User Name: ")
    pwd = getpass("Password: ")

    with open("users_and_pass.txt", "a") as file:

        file.write(f"{user}, {pwd}\n")

    print("Account created successfully!")

create_account()