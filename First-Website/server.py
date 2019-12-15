#server.py
#Source: https://www.youtube.com/watch?v=Lbfe3-v7yE0

import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    while True:
        cliensocket, address = s.accept()
        print(f"Connection from  {address} has been established!")
        cliensocket.send(bytes("Welcome to the server!", "utf-8"))