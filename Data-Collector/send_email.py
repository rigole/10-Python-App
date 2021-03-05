from email.mime.text import MIMEText

def send_email(email, height):
     from_email="foplacide@gmail.com"
     from_password="pythonlecture"
     to_email=email

     subject="height data "
     message="Hey there, your height is <strong>%s</strong>." % height

     msg=MIMEText(message, 'html')
     msg['Subject']=subject
     msg['To']=to_email
     msg['From']=from_email

     #gmail= smtplib.SMTP('smtp.gmail.com', 587)