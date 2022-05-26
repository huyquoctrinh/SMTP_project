import sys
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

def send_email(sender,receivers,password,content,subject):
    SMTP_Host = 'smtp.gmail.com'
    # sender = 'thaovo2962002@gmail.com'
    # receivers = ['trnhquchuy@gmail.com']
    # username = "thaovo2962002@gmail.com"
    # password = "a2k46pbc"
    # typical values for text_subtype are plain, html, xml
    text_subtype = 'plain'
    # content = """
    # Gui mail cho beo thanh cong
    # """
    # subject = "Thu ti"
    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject'] = subject
        msg['From'] = sender  # some SMTP servers will do this automatically, not all
        conn = SMTP(SMTP_Host)
        conn.set_debuglevel(False)
        conn.login(sender, password)
        try:
            conn.sendmail(sender, receivers, msg.as_string())
        finally:
            conn.quit()
    except Exception as error:
        print(error)
    
send_email("thaovo2962002@gmail.com",["trnhquchuy@gmail.com"],"a2k46pbc","hello","test")