import socket

# 클라이언트 소켓 생성
s_sock = socket.socket()
host = "localhost"
port =

# 서버에 연결

# 서버에 "I am ready" 메시지 전송

# 서버로부터 파일 이름 수신
fn = s_sock.recv(1024).decode()

# 파일을 "recv"라는 이름으로 현재 디렉토리에 저장
with open("./dummy" + "recv", "wb") as f:
    print("Receiving")
    while True:
        data = s_sock.recv(8192)
        if not data:
            break
        f.write(data)

print("Download complete")
s_sock.close()