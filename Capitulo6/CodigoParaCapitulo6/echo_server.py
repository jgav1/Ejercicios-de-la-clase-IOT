import socket
from wsgiref.simple_server import server_version

#Create a TCP/IP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('192.168.1.70', 999)

print("Starting up on {} port {}".format(*server_address))
sock.bind(server_address)

#Listen for incoming connections
sock.listen(1)


while True:
    #Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()

    try:
        print("connection from", client_address)

        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else: print("no data from", client_address)
            break

    finally:
        #Clean up the connection
        print("Closing current connection")
        connection.close()