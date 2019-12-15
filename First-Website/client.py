#client.py
#Source: https://www.youtube.com/watch?v=Lbfe3-v7yE0

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))