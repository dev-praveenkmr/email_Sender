import smtplib

e=input('Enter your Email:')
p=input('Enter your Password:')

try:
    s=smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()
    s.login(e,p)
    s_mail=input('enter the email id for reciever:')
    msg=intput('enter the message')
    s.sendmail(s_mail,e,msg)
    s.exit()
    print('message sended')

except:
    print('id or password are not correct')
