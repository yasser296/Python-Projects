from email.mime.text import MIMEText
from subprocess import Popen, PIPE

msg = MIMEText("Python & sendmail email test 01.")
msg["From"] = "yasser.ahmed98629@gmail.com" # Update to your test email address
msg["To"] = "yasser.ahmed98629@gmail.com" # Update to your test email address
msg["Subject"] = "Python & sendmail email test 01"
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msg.as_string())
print("Email sent!")
