import socket

# create server socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# get local Machine name

host = socket.gethostname()

# PORt

port = 9999

# bind the port
serverSocket.bind((host, port))

# Queue up to 5 queries

serverSocket.listen(5)


while True:
    # establish a connection
    clientSocket, address = serverSocket.accept()

    print("Got a connection from %s" % str(address))

    msg = 'Thank you for connecting' + "\r\n"
    clientSocket.send(msg.encode('ascii'))
    clientSocket.close()
