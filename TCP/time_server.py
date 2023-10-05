import socket
import time

# TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5000)
s.bind(address) # 소켓과 주소 결합
s.listen(5) # 연결 대기. 5개까지 동시 수용

client, addr = s.accept() # 연결 허용

while True:
    print("Connection requested from ", addr)
    client.send(time.ctime(time.time()).encode()) # 현재 시간 전송