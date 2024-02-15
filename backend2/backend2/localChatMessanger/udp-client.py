import socket
import sys
import os
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "/tmp/udp_socket_file"

address = "/tmp/udp_client_socket_file"

# 既存のソケットファイルを削除
try:
    os.unlink(address)
except FileNotFoundError:
    pass  # ファイルが存在しない場合は何もしない
message = input("サーバに送信するメッセージを入力してください: ")

try:
    sock.bind(address)  # ソケットをバインド
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    print(f"sending {message}")
    message = message.encode()
    sent = sock.sendto(message, server_address)

    print("サーバからの応答待ち")
    data, server = sock.recvfrom(4096)
    data = data.decode('utf-8')
    print("サーバから受け取ったメッセージ {!r}".format(data))
finally:
    print("ファイルを消去")
    sock.close()
    os.unlink(address)
    