from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendmail(to_addr, subject, msg_content, msg_type):

    from_addr = 'testmai1@sina.com'
    password = 'testmai1'
    smtp_server = 'smtp.sina.com'

    msg = MIMEText(msg_content, msg_type, 'utf-8')
    msg['From'] = _format_addr('xinali <%s>' % from_addr)
    msg['To'] = _format_addr('info <%s>' % to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    if to_addr:
        server = smtplib.SMTP(smtp_server, 25) 
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
