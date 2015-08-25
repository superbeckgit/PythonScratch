# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:42:07 2015

@author: mjbeck
"""

# Import smtplib for the actual sending function
#import smtplib
import win32com.client as win32

# Import the email modules we'll need
from email.mime.text import MIMEText

textfile = 'H:\Code\Perl\perl_notes.pl'
you = "dstauffman@gmail.com"
me = you
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(textfile) as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
#s = smtplib.SMTP('denmail.us.lmco.com')
#s.login("","")
#s.send_message(msg)
#s.quit()



outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = you
mail.Subject = 'Message sent via python'
mail.body = """I'm playing around with emails sent from python programs.
Since I don't know if LM has an SMTP server let alone what its name or address is I'm doing it
via the win32com library. There's the drawback that outlook doesn't like being manhandled so
it pops up a warning box about an automatic email and I have to click 'Accept', but then again,
all my outlook emails have the security popup so it will always require some human interaction.
Alternatively, I could set up an AutoIT script to watch for the warning pop-up, accept it, then
dismiss the security pop-up as well.
How was mexico?

-Matt  """
mail.send


print('done')
