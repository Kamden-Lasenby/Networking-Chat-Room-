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

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port " + str(port))

        s.bind((host,port))
        s.listen(5)
    
    except socket.error as err:
        print("Socket Binding error" + str(err) + "\n" + "Retrying:")
        # Recusively try binding again
        bind_socket()

# Establish connection with a client (socket must be listening)
    
def socket_accept():
    connection , address = s.accept()
    print("Connection has been established: " + " IP " + address[0] + " Port " + str(address[1]))
    
    connection.close()