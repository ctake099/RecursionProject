import socket

import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "/tmp/socket_file"
print("connection to {}".format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    # プログラムがエラーで終了したことを示すステータスコード
    sys.exit(1)

# サーバに接続出来たら、サーバにメッセージを送信
try:
    message = b"Sending a message to the server side"
    sock.sendall(message)

    sock.settimeout(2)

    try:
        while True:
            data = str(sock.recv(32))

            if data:
                print("Server response: " + data)
            else:
                break
    except(TimeoutError):
        print("Socket timeout")

finally:
    print("closing socket")
    sock.close()