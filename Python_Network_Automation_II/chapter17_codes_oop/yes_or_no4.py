from getpass import getpass

def get_credentials():
    #Prompts for, and returns a username1 and password1
    username1 = input("Enter Network Admin1 ID: ") # Request for username 1
    password1 = getpass("Enter Network Admin1 PWD: ") #  Request for password 1
    print("Username1 :", username1, "Password1 :", password1) # Print username and password

    #Prompts for  username2 and password2
    yes_or_no = input("Network Admin2 credentials same as Network Admin1 credentials? (Yes/No): ").lower() # Ask if Network Admin 2 has the same credentials as Admin 1
    expected_response = ['yes', 'y', 'no', 'n'] # Expect any of these four responses
    while yes_or_no not in expected_response: # Prompt until ‘yes’ or ‘no’ response is given
        yes_or_no = input("Expecting yes or no : ")
    if yes_or_no == "yes" or yes_or_no == "y": # If ‘yes’ or ‘y’, credentials are the same as Admin1
        username2 = username1
        password2 = password1
        print("Username2 :", username2, "Password2: ", password2) # Print username and password
    else: # If ‘no’ or ‘n’, request for Admin2 username and password
        username2 = input("Enter Network Admin2 ID : ")
        password2 = getpass("Enter Network Admin2 Password : ")
        print("Username2 :", username2, "Password2 :", password2) # Print username and password
get_credentials()
