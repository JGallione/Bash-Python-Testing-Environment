from __future__ import absolute_import, division, print_function, unicode_literals


import time
import os
import nltk
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub
import tensorflow_datasets as tfds

train_data, validation_data, test_data = tfds.load(
    name="imdb_reviews", 
    split=('train[:60%]', 'train[60%:]', 'test'),
    as_supervised=True)

train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))
print (train_examples_batch)
print (train_labels_batch)

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

