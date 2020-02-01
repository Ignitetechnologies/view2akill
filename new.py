#!/usr/bin/python 
# -*- coding: UTF-8 -*- 
import string 
from hashlib import sha1 
import requests 
fuzz=[] 
for alpha in string.ascii_lowercase:
  for a in string.digits:
    for b in string.digits:
      payload= sha1((alpha + "view" + a + b + "\n").encode("utf-8")).hexdigest()
      fuzz.append(payload) 
file1 = open("directories.txt","w") 
for i in fuzz:
  file1.write(i)
  file1.write("\n") 
file1.close()
