# autoMail [![Build Status](https://travis-ci.org/tlpss/autoMail.svg?branch=master)](https://travis-ci.org/tlpss/autoMail)


*Quick solution for sending dynamic mails (html templates) over the free google smtp server*

## setup
* clone the repo on your pc (if you don't know how to do this it might be usefull to have someone helping you that has a little more experience with this kind of shit, or you can just google it)
* copy `configuration_template.py` to `configuration.py`
* fill in your google account
* create an application password for your google account and put it in the configuration (keep this pwd secret!)
cf. https://support.google.com/accounts/answer/185833?hl=en

N.B. if you want you can just create env variables instead of copying this file

## usage (suggested workflow, alternatives are most certainly possible)

* create a new folder 
* create your mail layout in word/ gmail and convert it to HTML (https://wordhtml.com/) 
* create the html file inside the folder
* create a csv with all receivers and the template data (if any), the data should be in order of usage
* create a new main.py and configure everything as you wish ( see docstring in the code for more info about the different fields)
* run the main.py 
* check if the output is as expected (no addresses skipped or malformed)

## Templating

the html file may contain "personal" fields, such as the company name. 
Any `{<name>}` in the html will be considered such a templated field and will be replaced by the corresponding column entry in the csv. 
Keep in mind that the order of appearance of these fields should match the order in the csv file.

## Example

The repo contains an example (Internshipfair) of how to send a mail with an attachment and a template containing the company name.
Furthermore a BCC address is used and the Testflag is set to True, which allows to perform a final check on the first csv entry (this should hence be your own mailaddress)
