import socket
import time
import struct

testing_strings = ["E1.0 -945 1689 -950 230 -25 1", "S0 2 -945 1689 -950 230 -25 1 1e-15", "G4.1 0 0", "4 1 0", "E1.0",
                   "S1.0", "S0 2 -945 1689 -950 230 -25 1 -1e-15", "Not a number", "S0 2 -945 1689 -950 230 -25 1 0",
                   "S0 2 -945 1689 -950 230 G 1 1e-15"]

# # 1. create a socket
# sock = socket.socket()
#
# # 2. Make a connection to the server
# sock.connect(('127.0.0.1', 12345))

for string in testing_strings:
    # 1. create a socket
    sock = socket.socket()

    # 2. Make a connection to the server
    sock.connect(('127.0.0.1', 12345))


    # request = input("Enter a request to test: ")
    request = string
    request_byte = request.encode(encoding='UTF-8',errors='strict')

    # 3. Send a request to the server
    # sock.sendall(request_byte)
    sock.sendall(struct.pack("i", len(request_byte)) + request_byte)
    # sock.shutdown(1)
    time.sleep(1)

    print("sent")


# 4. receive a response from the server
bytes = sock.recv(2048)
response=""
while len(bytes)>0:
    response=bytes.decode(encoding='UTF-8',errors='strict')
    bytes=sock.recv(2048)
print("Server response " + response)

# 5. close the socket
sock.close()
