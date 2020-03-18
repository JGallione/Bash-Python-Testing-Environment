import time
import os
import nltk

print ("hello")

Service_Ticket = input ("Enter Ticket:")

VPN_Arr = ["vpn", "VPN"]
Adobe_Arr = ["Adobe", "adobe", "ADOBE", "PDF", "pdf"]

if any(c in Service_Ticket for c in VPN_Arr):
    print ("contains vpn")
elif any(c in Service_Ticket for c in Adobe_Arr):
    print ("contains adobe")
else:
    print ("does not contain key words: vpn or adobe")

