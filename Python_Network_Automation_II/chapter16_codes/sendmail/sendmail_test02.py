import smtplib

sender = 'yasser.ahmed98629@gmail.com'
receivers = ['yasser.ahmed98629@gmail.com']

message = """
From: No Reply <no_reply@italchemy.com>
To: Python Network Automation <pynetauto@gmail.com>
Subject: Sendmail SMTP Email test 01

This is a Sendmail SMTP Email test 01
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")
