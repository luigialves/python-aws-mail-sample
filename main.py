import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "me@mail.com"
to = "to@mail.com"

# AWS Config
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

msg = MIMEMultipart('alternative')
msg['Subject'] = "Subject Test"
msg['From'] = sender
msg['To'] = to

html = open('index.html').read()

mime_text = MIMEText(html, 'html')
msg.attach(mime_text)

s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
s.starttls()
s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
s.sendmail(sender, to, msg.as_string())
s.quit()