import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

sender_email = "" # add your email here
password = ''     #add your app password here
subject = "Inspirational quotes"


message = MIMEMultipart()
message['From'] = sender_email
message['To'] = sender_email
message['Subject'] = subject

with open("Business Cliches.txt", "r") as file:
     cliches = file.readlines()

body= random.choice(cliches)
message.attach(MIMEText(body, 'plain'))     

message_string = message.as_string()

#Send email with smtp library

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(
         from_addr=sender_email, 
         to_addrs=sender_email, 
         msg=message_string
         )