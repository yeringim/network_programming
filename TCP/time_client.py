import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)
sock.connect(address) # 서버 연결

while True:
    time.sleep(1)
    print("현재 시각: ", sock.recv(1024).decode()) # 수신 내용을 문자열로 변환하여 출력