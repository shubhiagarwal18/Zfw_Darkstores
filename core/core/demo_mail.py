import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('anubhav.april01@gmail.com','Anubhav@1234')
server.sendmail('anubhav.april01@gmail.com', 'shubhimay18@gmail.com', 'Mail sent from python')
print("mail sent")