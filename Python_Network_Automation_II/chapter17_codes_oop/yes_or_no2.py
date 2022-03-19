def yes_or_no():
    yes_or_no = input("Enter yes or no : ")
    yes_or_no = yes_or_no.lower()
    if yes_or_no == "yes" or yes_or_no == "y": # Takes abbreviated response
        print("Oh Yes!")
    elif yes_or_no == "no" or yes_or_no == "n": # Takes abbreviated response
        print("Oh No!")
    else: # Any other responses, print the following statement
        print("You have not entered the correct response.")
yes_or_no()
