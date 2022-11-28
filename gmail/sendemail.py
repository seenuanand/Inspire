import smtplib

server = smtplib.SMTP('smtp.googlemail.com', 587)

server.starttls()
server.login('srinivas.anand9999@gmail.com','xxrqzgzqeaxwhvjn')
server.sendmail('srinivas.anand9999.gmail.com', 'srinivas.anand1@gmail.com','Mail sent from python')
print('Mail Sent')