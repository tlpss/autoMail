import unittest
from mail_system import *

class SimpleTests(unittest.TestCase):
    def test_mailer(self):
        server = create_connection()
        print("connection created")
        res = send_mail("thomas.lips@ugent.be","thomas17.lips@gmail.com",None,"test","<p>test</p>",
                        [],server)
        close_connection(server)
        self.assertEqual(res, 0)

    def test_mail_system(self):
        res = bunch_mailer("career@vtk.ugent.be","TEST BUNCH", "Test/resources/example.html", [], None , "Test/resources/config.csv", test = False)
        self.assertEqual(res,0)

