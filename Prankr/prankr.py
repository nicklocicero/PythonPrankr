# Prankr
# version 0.0.1
# use twilio to create and send prank sms and voice calls

# import prank Class templates
from templates import *
import templates

# import list of pranks
from prankslist import *
import prankslist

# get users choice to send or save new prank
def user_start(prank_list):

    print "1: get list of pranks\n2: create a new prank"
    user_choice = raw_input("1 or 2: ")

    if user_choice == "1":
        send_prank_sms(prank_list)

    if user_choice == "2":
        create_new_prank()

    if user_choice != "1" and user_choice != "2":
        print "please try again with 1 or 2"

# function for sending the prank, called if user inputs 1
def send_prank_sms(prank_list):

    print prank_list

    text_to_send = raw_input("type which prank to send without any quotes, just the exact name: ")
    number_to_send_to = raw_input("what are the ten digits for the mobile number? ")

    if text_to_send not in prank_list:
        print "error: use correct name"

    for i in prankslist.pranks:
        if i.title == text_to_send:
            print "working.."
            i.send_sms(number_to_send_to)
            print "message sent. mwuaahahaha."

# function for creating new prank, called if user inputs 2
def create_new_prank():

    user_title = raw_input("Name prank title without spaces: ")
    user_body = raw_input("What should the body of the prank be? ")

    if " " in user_title:
        print "don't use spaces"
        return

    # open prank python file that has templates
    prank_templates_read = open('templates.py', 'r')
    # save text of python templates file in variable
    prank_templates_save = prank_templates_read.read()

    # open prank python files again, but this time for writing
    new_prank_templates = open('templates.py', 'w')
    # create new file using old file text + new prank
    new_prank_templates.write(prank_templates_save+user_title+" = base.Sms(" + "'"+ user_title + "'" +","+"'"+user_body+"'"+")\n\n")
    
    # same as above, but this updates the prankslist.py file
    prank_list = open("prankslist.py", "r")
    prank_list_read = prank_list.read()
    prank_list_save = open("prankslist.py", "w")
    prank_list_save.write(prank_list_read[0:len(prank_list_read)-2] + ', ' + user_title + "]")

    # confirm user has saved new prank
    print "New prank " + user_title + " saved."

# create list of pranks
pranks = []
for i in prankslist.pranks:
    pranks.append(i.title)

# initiate pranks
user_start(pranks)
