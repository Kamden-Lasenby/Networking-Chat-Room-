import socket
import sys

# Create a Socket ( connect two computers )
def create_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as err:
        print("Socket creation error: " + str(err))