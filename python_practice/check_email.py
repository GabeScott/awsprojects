import poplib
import os
from email.parser import Parser

user = 'recent:gabescottaws@gmail.com'
Mailbox = poplib.POP3_SSL('pop.gmail.com', '995')
Mailbox.user(user)
Mailbox.pass_('Gamecubekingaws')

resp, mails, octets = Mailbox.list()

index = len(mails)

for i in range(index):
    resp, lines, octets = Mailbox.retr(i+1)
    content = b'\r\n'.join(lines).decode('utf-8')
    message = Parser().parsestr(content)

    body = ''

    if message.is_multipart():
        for part in message.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode = True)
    else:
        body = message.get_payload(decode=True)
    
    body = body.replace('\n', ' ')
    body = body.replace('\r', '')

    if message['Subject'] == 'crontab':
        os.system('crontab -l > tempfile')
        os.system('echo \'' + body + '\' >> tempfile')
        os.system('crontab tempfile')
        os.system('rm tempfile')
 
    Mailbox.dele(i+1)
    
Mailbox.quit()


