from faker import Faker
import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = "/tmp/udp_socket_file"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"ソケットが起動しています address -> {server_address}.")

sock.bind(server_address)

while True:
    print("\nメッセージを待っています")
    data, address = sock.recvfrom(4096)
    data = data.decode('utf-8')
    print(f"受信したデータのバイト数 {len(data)} from {address}")
    print("data : ", data)

    if data:
        faker = Faker()
        fake_address = faker.address().encode()
        sent = sock.sendto(fake_address, address)
        # sent = sock.sendto(data, address)
        print(f"sent {sent} bytes back to {address}")