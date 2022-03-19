import smtplib

sender = 'no_reply@italchemy.com'  # A variable, sender
receivers = ['pynetauto@gmail.com'] # A variable, receivers. Add more emails using comma separator

# This is the main message which will be sent to the email recipient(s). Anything between the triple quotes
message = """
From: No Reply <no_reply@italchemy.com>
To: Python Network Automation <pynetauto@gmail.com>
Subject: SW1 not reachable for more than 30 seconds

SW1 is not reachable. Please investigate.
"""

def send_email(): # Define send_email function
    try:
       smtpObj = smtplib.SMTP('localhost') # Define smtpObj
       smtpObj.sendmail(sender, receivers, message) # Send an email using smtpObj and variables
       print("Successfully sent email")  # Informational
    except SMTPException: # SMTP Exception
       print("Error: unable to send email")  # Informational
