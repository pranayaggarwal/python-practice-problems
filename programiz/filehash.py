# Python rogram to find the SHA-1 message digest of a file

# importing the hashlib module
import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Picture1.jpg"
abs_file_path = os.path.join(script_dir, rel_path)

print("Full file path is", abs_file_path)
print("file hash is", hash_file(abs_file_path))