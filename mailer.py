"""
this file contains the actual mailing function
"""
from configuration import Configuration
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from os.path import  basename
import os

def create_connection():
    """
    creates TLS connection with gmail smtp server
    :return: server object
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(Configuration.user, Configuration.app_pwd)

    return server


def close_connection(server):
    server.close()


def send_mail(sender_mail, receiver_mail, bcc_mail, subject, html_text, attachment_files, server):
    """
    uses an open tls server connection to send the specified
    :param sender_mail: exact one mail address (string)
    :param receiver_mail: exact one mail address (string)
    :param bcc_mail: one mail address (string) or None
    :param subject: string
    :param html_text: string containing html file
    :param attachment_files: list of files to attach (strings)
    :param server: open connection to the server
    :return: 0 (OK) or -1 (NOK)
    """

    # create message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_mail
    message["To"] = receiver_mail
    if bcc_mail is not None:
        message["Bcc"] = bcc_mail

    # add text
    html_mime = MIMEText(html_text, 'html')
    message.attach(html_mime)

    # add attachments
    for file in attachment_files:
        path = file
        print(path)
        with open(path, "rb") as f:
            ext  =file.split('.')[-1:]
            attachedfile = MIMEApplication(f.read(), _subtype = ext)
            attachedfile.add_header('content-disposition', 'attachment', filename = basename(file))
        message.attach(attachedfile)

    # send mail
    try:
        server.send_message(message)
        return 0
    except:
        return -1
