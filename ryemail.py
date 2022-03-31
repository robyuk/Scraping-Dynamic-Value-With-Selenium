import yagmail
import os
import time

sender='automailry@gmail.com'
receiver='3b4mzwq7@freeml.net'
subject='CBX has dropped'
content="""
This is the email content
on multiple lines

"""

i=1
yag=yagmail.SMTP(user=sender, password=os.getenv('automailrypw'))

while True:
    yag.send(to=receiver, subject=subject, contents=content+str(i))
    print("Email ", i, " sent.")
    i=i+1
    time.sleep(60)
