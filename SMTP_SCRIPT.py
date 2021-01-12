import smtplib
from email.mime.text import MIMEText

#body="Good e evening sir sir\nSir I m fucusing issue while running server chat and client chat with socket look at the error 'OSError: [Errno 107] Transport endpoint is not connected' can you please help me to solve it out?\nif you receive this enail that means I used 'SMTPLIB' in python"
body="Good morning Sir\nThis morning I solved my issue about the previous email that I sent you\nThank you sir and Have a nice day\nFrom SMTPLIB script. "
message=MIMEText(body)

fromAddr="yateassekeronald@gmail.com"

toAddr='etrainerit@gmail.com'

#message['From'] = "YATE <{}>".format(fromAddr)
#message['To'] = ',, '.join(toAddr)
message['From'] =fromAddr
message['To'] = toAddr
message["Subject"]="Issue with chat_programming with socket"

server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

password='yate1999Y,'
server.login(fromAddr,password)

server.send_message(message)

print("message sent......")

server.quit()


