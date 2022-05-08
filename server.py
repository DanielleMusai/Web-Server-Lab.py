#import socket module
from socket import *

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM) # Create a TCP server socket
# Prepare a sever socket
# Fill in start
serverSocket.bind(("10.0.0.13",serverPort)) #connecting the socket to port 6789
serverSocket.listen(1) #listen to the client request
print('The server is ready to receive:', serverPort)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # Fill in start   #Fill in end #the server wait to a connecting request from the client
    try:
        message = connectionSocket.recv(1024).decode() # Fill in start #Fill in end #read a bytes from the socket
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  # Fill in start #Fill in end
        print(outputdata)
        # Send one HTTP header line into socket
        # Fill in start#
        connectionSocket.send('\nHTTP/1.0 200 OK\n\n'.encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("\nHTTP/1.0 404 Not Found\n\n".encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
    # Fill in end
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
