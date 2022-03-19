from getpass import getpass

def get_credentials():
    #Prompts for, and returns a username1 and password1
    username1 = input("Enter Network Admin1 ID: ") # Request for username 1
    password1 = None  # Set password1 to None (initial value to None)
    while not password1: # Until password1 is given
        password1 = getpass("Enter Network Admin1 PWD : ")  # Get password1
        password1_verify = getpass("Confirm Network Admin1 PWD : ")  # Request for validation
        if password1 != password1_verify: # If the password1 and verification password does not match
            print("Passwords do not match. Please try again.") # Print this information
            password1 = None  # Set the password to None and ask for password1 again
    print("Username1 :", username1, "Password1 :", password1) # Print username and password

    #Prompts for  username2 and password2
    yes_or_no = input("Network Admin2 credentials same as Network Admin1 credentials? (Yes/No): ").lower() # Ask if Network Admin 2 has the same credentials as Admin 1
    expected_response = ['yes', 'y', 'no', 'n'] # Expect any of these four responses
    while yes_or_no not in expected_response: # Prompt until ‘yes’ or ‘no’ response is given
        yes_or_no = input("Expecting yes or no : ")
    if yes_or_no == "yes" or yes_or_no == "y": # If ‘yes’ or ‘y’, credentials ate the same as Admin1
        username2 = username1
        password2 = password1
        print("Username2 :", username2, "Password2 :", password2) # Print username and password

    else: # If ‘no’ or ‘n’, request for Admin2 username and password
        username2 = input("Enter Network Admin2 ID: ") # Request for username 2
        password2 = None  # Explanation same as above
        while not password2: # Explanation same as above
            password2 = getpass("Enter Network Admin2 PWD : ") # Explanation same as above
            password2_verify = getpass("Confirm Network Admin2 PWD : ")
            if password2 != password2_verify: # Explanation same as above
                print("Passwords do not match. Please try again.")
                password2 = None # Explanation same as above
        print("Username2 :", username2, "Password2 :", password2) # Print username and password

get_credentials()
