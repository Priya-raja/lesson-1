import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders  
import random


sender_email = "" # add your email here
receiver_email = "" # add the receiver email here
password = ''     #add your app password here
subject = "Daily Dose of Inspiration"


message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email # add the receiver email here
message['Subject'] = subject    

with open("Business Cliches.txt", "r") as file:
     cliches = file.readlines()
body = random.choice(cliches)   
message.attach(MIMEText(body, 'plain'))


with open("airhorn.mp3", "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=airhorn.mp3')
    message.attach(part)

message_string = message.as_string()

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(
         from_addr=sender_email, 
         to_addrs=receiver_email, 
         msg=message_string
         )