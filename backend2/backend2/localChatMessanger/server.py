# クライアントはサーバにメッセージを送り、
# それに対する応答を待ちます。
# これは一種の「質問と応答」のパターンであり、
# クライアントがメッセージを送り、サーバがそれに応答する

import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = "/tmp/socket_file"

try:
    # 以前の接続が残っていた場合に備えて、サーバアドレスをアンリンク（削除）します
    os.unlink(server_address)
except FileNotFoundError:
    pass

print("starting up on {}".format(server_address))

# server_addressで待っている
sock.bind(server_address)

# 接続を待っている
sock.listen(1)

# クライアントからの接続を待ち続けます
while True:
# connection: これは新しく確立されたクライアントとの接続を表す新しいソケットオブジェクトです。このオブジェクトを通じて、サーバーはクライアントとデータを送受信します。
# client_address: これは接続してきたクライアントのアドレス情報です。インターネットソケットの場合、これはクライアントのIPアドレスとポート番号のタプルです。UNIXドメインソケットの場合、クライアントの具体的なアドレス情報は異なるか、あるいは空になることがあります。   
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)

        while True:
            # 一度に読み込むバイト数
            data = connection.recv(16)
            data_str =  data.decode('utf-8')
            print('Received ' + data_str)

            if data:
                response = "Processing " + data_str
                connection.sendall(response.encode())
            else:
                print("no data from", client_address)
                break
    finally:
        print("Closing current connection")
        connection.close()
