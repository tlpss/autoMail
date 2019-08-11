import pytest
from mailer import *
from mail_system import *

def test_mailer():
    server = create_connection()
    print("connection created")
    res = send_mail("thomas.lips@ugent.be","thomas17.lips@gmail.com",None,"test","<p>test</p>",
                    ["Turing_Paper_1936.pdf"],server)
    close_connection(server)
    assert  res == 0

def test_mail_system():
    res = bunch_mailer("career@vtk.ugent.be","TEST BUNCH", "example.html", [], None , "config.csv")
    assert res == 0