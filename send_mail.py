import smtplib

# MAKE SURE to go to the gmail page after an initial error; google does not
# recognize this as a valid application. You should get an email about this,
# simply follow through the steps to add this application as a trusted
# application.
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jxp604@gmail.com'
recipient = 'xpian@yelp.com'
subject = 'Gmail SMTP Test'
body = 'blah blah blah'

"Sends an e-mail to the specified recipient."

body = "" + body + ""

headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)

session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()
