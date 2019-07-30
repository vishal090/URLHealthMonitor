import requests
import smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
import os

fromaddr = "<<Enter your email address here>>"

url = 'http://dehensv613.de.henkelgroup.net:20081/chk_status'

page = requests.get(url, timeout=90)

soup = BeautifulSoup(page.content, 'html.parser')

print("***DEHENSV613:81 POD***")

for lvl in soup.select('tests'):
    print("The startup date is ", lvl['date'])

for lvl in soup.select('test'):
    if lvl['id'] == 'sys.disk':
        if lvl['level'] == "wrn" or lvl['level'] == "err":
            print("The disk is at warning ", lvl.percent['value'])
        else:
            print("The disk is at normal level ", lvl.percent['value'])

for lvl in soup.select('test'):   
    if lvl['id'] == 'sys.mem':
        if lvl['level'] == "wrn" or lvl['level'] == "err":
            print("The memory is at warning ", lvl.percent['value'])
        else:
            print("The memory is at normal level ", lvl.percent['value'])

for lvl in soup.select('test'):
    if lvl['id'] == 'sys.thread':
        if lvl['level'] == "wrn" or lvl['level'] == "err":
            print("!!The thread level is at warning!!")
            print("The total thread value is ", lvl.total['value'])
            print("The running thread value is ", lvl.running['value'])
            print("The jobs value is ", lvl.jobs['value'])
        else:
            print("The thread is at normal level ", lvl.running['value'])


msg = MIMEMultipart()

msg['From'] = fromaddr
msg['Subject'] = "POD Thread count notification mail"

filename = 'thread_count.txt'
attachment = open('/root/environments/python_progs/thread_count.txt','r')

part = MIMEApplication(attachment.read(), Name=os.path.basename(filename))
encoders.encode_base64(part)
part['Conetnt-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(filename))

msg.attach(part)

text = msg.as_string()

for lvl in soup.select('test'):
    if lvl['id'] == 'sys.thread':
        if lvl['level'] == "wrn" or lvl['level'] == "err":
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(fromaddr, "<<Enter your email address password here>>")
            server.sendmail(fromaddr,["<<Enter the list of recepients email address here>>"],text)
            server.quit()
            print("Mail Sent")


