import sys
from smtplib import SMTP_SSL as SMTP      
from email.mime.text import MIMEText

class Sender:
    def __init__(self,uname,passw):
        self.SMTP_Host = 'smtp.gmail.com'
        self.sender = uname
        self.conn = SMTP(self.SMTP_Host)
        self.conn.set_debuglevel(False)
        self.conn.login(uname, passw)
    def send(self,content,subject,receivers):
        try:
            text_subtype = 'plain'
            msg = MIMEText(content, text_subtype)
            msg['Subject'] = subject
            msg['From'] = self.sender  
            try:
                self.conn.sendmail(self.sender, receivers, msg.as_string())
                print("Send success")
            finally:
                self.conn.quit()
        except Exception as error:
            print("Some thing wrong")
            print(error)
