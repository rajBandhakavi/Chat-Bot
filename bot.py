##
# This module is the interface with the humans. It takes in English language,
# decides which module should deal with this, and reurns the response back in English Language
# Integrations with Slack, Messenger, SMS or anything else can be done here
##
from job_search1 import *
 
while True:
    message = input(">> ")
    if message == "stop":
        break
    else:
        print(handle_message(message))