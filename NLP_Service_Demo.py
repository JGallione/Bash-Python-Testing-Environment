import os
import time
import tensorflow
import nltk

print ("hello")

Service_Ticket = input ("Enter Ticket:")

VPN_Arr = ["vpn", "VPN"]

if any(c in Service_Ticket for c in VPN_Arr):
    print ("contains vpn")
else:
    print ("does not contain vpn")

raw_input = input ('Press Enter to exit')
