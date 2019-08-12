"""
this file sends all mails according to specified input
"""
import pandas as pd
from os.path import join
from mailer import *
import numpy as np
#TODO: mail & attachments folder to configuration


def bunch_mailer(sender_mail, subject, html_file, attachments, bcc_mail, configuration_csv, test = False):
    """

    :param sender_mail:
    :param subject:
    :param html_file: may contain variables in {}!
    :param attachments:
    :param bcc_mail:
    :param configuration_csv: a csv with header that contains the receiver(first column) and then the params for the html
    :param test: if True: the mail is sent to the first person in the config_csv only giving you the possibility to verify everything is as expected
                only if you press continue the mail is sent to all other persons
    :return: 0 if successful
    """
    data = pd.read_csv(join(Configuration.mail_folder,configuration_csv))
    columns = (list(data))

    # read html
    with open(join(Configuration.mail_folder,html_file), "r") as html:
        html_text = html.read()

    # open connection
    server = create_connection()

    # create mails

    for index,row in data.iterrows():
        # fill in variables in html
        arg_dict = {}
        for arg in columns[1:]:
            if data[arg][index] is np.nan:
                arg_dict[arg] = ""
            else:
                arg_dict[arg] = data[arg][index]

        formatted_html = html_text.format(** arg_dict)
        print(f"sending to {data[columns[0]][index]}")
        # send mail
        send_mail(sender_mail,data[columns[0]][index],bcc_mail,subject,formatted_html,attachments,server)

        # allow for check if required
        if index is 0 and test:
            res = input("The first mail was sent, please verify everything is as expected \n If so, type \"yes\" and press enter\n")
            if not res == "yes":
                return -1
    # close connection

    close_connection(server)
    return 0


if __name__ == "__main__":
    bunch_mailer("career@vtk.ugent.be", "TEST BUNCH", "example.html", [], None, "config.csv", test=True)