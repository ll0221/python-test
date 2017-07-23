#!/usr/bin/python

yn = raw_input("Please input [Yes/No]:")
yn = yn.lower()

if yn == 'y' or yn == 'yes': 
    print "You choose Yes"
elif yn == 'n' or yn == 'no': 
    print "You choose No"
else:
    print "Please input [Yes/No]:"
print "Over"
