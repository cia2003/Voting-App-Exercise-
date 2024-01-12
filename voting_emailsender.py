from email.message import EmailMessage
from abc import ABC, abstractmethod

import smtplib
import ssl

class IEmailSender(ABC):
    @abstractmethod
    def send_email(self, receiver: str, subject: str, body: str):
        pass

class EmailSender(IEmailSender):
    def send_email(self, receiver: str, subject: str, body: str):
        em = EmailMessage()
        em['From'] = "//fill this with your gmail account"
        em['To'] = receiver

        # set the subject and body of the email
        em['Subject'] = subject
        em.set_content = body

        # add ssl (layer of security)
        context = ssl.create_default_context()

        # log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login("//fill this with your gmail account", "fill this with your gmail password")
            smtp.sendmail("//fill this with your gmail account", receiver, em.as_string())