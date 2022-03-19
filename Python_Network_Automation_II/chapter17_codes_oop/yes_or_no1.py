def yes_or_no(): # Create function called yes_or_no
    yes_or_no = input("Enter yes or no : ") # Ask for user input
    yes_or_no = yes_or_no.lower()# change all input casing to lower casing
    if yes_or_no == "yes":  # if answer is ‘yes’ take the following action
        print("Oh Yes!")
    else: # if answer is ‘no’ or other input, take the following action
        print("Oh No!")
 
yes_or_no()  # Run the function
