from getpass import getpass  # Import getpass module from getpass library

def get_credentials():# Create get_credentials function
    #Prompts for and returns a username and password  
    username = input("*Enter Network Admin ID : ")  # Prompt user for username
    password = None  # Set original password to None
    while not password: # Keep prompting til password is entered
        password = getpass("*Enter Network Admin PWD : ")  # Prompt for password
        password_verify = getpass("**Confirm Network Admin PWD : ")  # Verify password again
        if password != password_verify: # If password fails to  verified, run the following script
            print("! Network Admin Passwords do not match. Please try again.") # Inform the user of mismatch
            password = None  # Reset password to None and ask for the password again
    print(username, password) # For testing purpose only, remove this when applied to the script
    return username, password  #returns username and password

get_credentials() # Run get_credentials() function
