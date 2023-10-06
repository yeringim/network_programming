import socket

BUFSIZE = 1024
port = 2500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("message: ")
sock.sendto(msg.encode(), ('localhost', port)) # 메시지 송신
data, addr = sock.recvfrom(BUFSIZE) # 메시지 수신
print("Server says: ", data.decode())