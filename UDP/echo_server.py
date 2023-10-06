import socket

port = 2500
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(BUFSIZE)
    print("Received message: ", data.decode())

    s_msg = input("message: ")
    sock.sendto(s_msg.encode(), addr)