from mail_system import *
def mail_system():
    res = bunch_mailer("career@vtk.ugent.be","Praktische info Internshipfair", "internshipfair.html",['internshipfair_guide_example.pdf'],"career@vtk.ugent.be", "internshipfair.csv", test=True)
    assert res == 0
    print("finished")

if __name__ == "__main__":
    mail_system()