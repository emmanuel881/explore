import smtplib
import getpass
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEMultipart

#define the smtp server ur using
HOST = "smtp-mail.outlook.com"
PORT = "587"

#we then create an smtp object
server = smtplib.SMTP(HOST, PORT)
print(server)

#we now can check if there is a connection
connect_status = server.ehlo()

print(connect_status)

#login to your email

myMail = "something@email.com"#your email
PASSWORD = getpass.getpass("Enter pass word: ")

server.login(myMail, PASSWORD)

#reciever's mail
toMail = "something@email.com"

#lets create a message
msg = MIMEMultipart()
#state the name you want to use
msg["From"] = "my name"
#the person you are sending the message to
msg["To"] = toMail
msg["Subject"] = "hello world"#message subject

with open('emailSendAuto.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, "plain"))

#lets attach an image
filename = "./someImage.jpg"#image location

attachment = open(filename, "rb")#reading the file

#create the payload object
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

#lets encode the payload
encoders.encode_base64(p)
p.add_header()
#lets add a header
p.add_header("Content-Disposition" f"attachment; filename={filename}")
#lets attach the payload now
msg.attach(p)

#lets convert to string
text = msg.as_string()
server.sendmail(myMail, toMail, text)

