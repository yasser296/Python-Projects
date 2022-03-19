#!/usr/bin/python3
from twilio.rest import Client # import required libraries and modules
import os
import re
import time
from time import strftime

current_time = strftime("%a, %d %b %Y %H:%M:%S") # Create your own time string format

account_sid = "ACe9c9ed26425723d4113f026bc87bd6e4" # Replace this with your own Twilio SID
auth_token = "2407186298268594f576d8fb72e1075b" # Replace this with your own Twilio token
my_smartphone = "+201271653370" # Replace this your own country code and Smartphone number
twilio_trial = "+19034857225" # Twilio trial number

device_hstname = "R1"
device_ip = "192.168.110.140"

cpu_util_value = str()

def send_sms(cpu_util_value): # Define send_sms function
    client = Client(account_sid, auth_token)
    my_message = f"High CPU utilization notice, Device: {device_hstname} IP: {device_ip} has reached {cpu_util_value}%, High CPU utilization. At time  {current_time} ."
    message = client.messages.create (body=my_message, from_=twilio_trial, to=my_smartphone)
    print(message.sid)

stream = os.popen(f'snmpwalk -v3 -l authPriv -u SNMPUser1 -a SHA -A "AUTHPass1"  -x AES -X "PRIVPass1" {device_ip} 1.3.6.1.4.1.9.9.109.1.1.1.1.5') # SNMPwalk command 
output = stream.read() # Read and capture output
time.sleep(3) # Pause script for 3 seconds
print("-"*80)
print(current_time, output) # Informational

with open('./cpu_oid_log.txt', 'a+') as f: # When manually run, writes to this file
    if "Gauge32:" in output: # Check if ‘Gauge32’ is in the output
        p1 = re.compile(r"(?:Gauge32: )(\d+)") # Positive look behind to locate CPU digit value
        m1 = p1.findall(output) # Find and match the digit
        cpu_util_value = m1[0] # Re findall returns value as a list, so index it to get it as an item
        if int(cpu_util_value) < 10: # If CPU utilization value is less than 90 ( 90%)
            f.write(f"{current_time} {cpu_util_value}%, OK\n'") # Write to file
            print("OK") # Write to cron.log
        elif int(cpu_util_value) >= 11: # If CPU utilization value is more than 90 ( 90%)
            f.write(f"{current_time} {cpu_util_value}%, High CPU\n'")
            print("High CPU") # Write to cron.log
            send_sms(cpu_util_value)
    elif "Timeout:" in output: # if ‘Timeout’ is in output, send an SMS
        f.write(f"{current_time} High CPU, Timeout: No Response\n'")
        print("Timeout: No Response") # Write to cron.log
        send_sms(cpu_util_value)
    elif "snmpwalk:" in output: # if ‘snmpwalk’ is in output, send an SMS
        f.write(f"{current_time} High CPU, snmpwalk: Timeout\n'")
        print("No Response") # Write to cron.log
        send_sms(cpu_util_value)
    else: # Everything else
        f.write(f"{current_time} High CPU utilization, IndexError\n")
        print("IndexError occured due to High CPU Utilization") # Write to cron.log
        send_sms(cpu_util_value)


print("Finished") # This should print when the script runs successfully.
