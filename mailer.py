"""
this file contains the actual mailing function
"""
from configuration import Configuration
import smtplib

def create_connection():
    """
    creates TLS connection with gmail smtp server
    :return: server object
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    print(1)
    server.ehlo()
    server.starttls()
    server.login(Configuration.user, Configuration.app_pwd)

def close_connection(server):
    server.close()

def send_mail(sender_mail, receiver_mail, bcc_mail, subject, html_text, attachment_files, server):
    """
    uses an open tls server connection to send the specified
    :param sender_mail: exact one mail address
    :param receiver_mail: exact one mail address
    :param bcc_mail: up to one mail address
    :param subject: string
    :param html_text: string containing html file
    :param attachment_files: list of files to attach
    :param server: open connection to the server
    :return: 0 (OK) or -1 (NOK)
    """

