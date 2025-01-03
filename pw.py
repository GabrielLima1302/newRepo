#!/usr/bin/env python3
#REMEMBER TO RUN : "chmod +x pythonScript.py" TO BE ABLE TO RUN THE SCRIPT IN THE TERMINAL
#MY PASSWORDS
PASSWORDS = { #Dictionary of accounts/passwords
    'email': 'aaa',
    'instagram' : 'bbb',
    'game':'ccc'
}
import sys
import pyperclip

if len(sys.argv) < 2: #Verify if there is only the ./script.py as a parameter
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1] #account receive the second parameter (the one after the ./script.py)

if account in PASSWORDS: #Looks in the PASSWORDS dictionary
    pyperclip.copy(PASSWORDS[account]) #copy the password from the key named as the String received by "account"
    print("Password for " + account + " copied to clipboard")
else:
    print("There is no account named " + account)

