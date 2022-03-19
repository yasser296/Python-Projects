def yes_or_no():
    yes_or_no = input("Enter yes or no : ").lower()
    expected_response = ['yes', 'y', 'no', 'n'] # Expected responses
    while yes_or_no not in expected_response: # Prompt until ‘yes’ or ‘no’ response is given
        yes_or_no = input("Expecting yes or no : ")
    if yes_or_no == "yes" or yes_or_no == "y":  # ‘yes’ or ‘y’ action
        print("Oh Yes!")
    else: # ‘no’ or ‘n’ action
        print("Oh No!")

yes_or_no()
