import socket

# サーバのIPアドレスとポート番号
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 9001

def receive_file(client_socket):
    # クライアントから送信されるファイルのバイト数を受信
    file_size_bytes = client_socket.recv(32)
    file_size = int(file_size_bytes.decode('utf-8'))

    # ファイルを受信
    received_bytes = bytearray() # 受信したデータを格納するバイト配列
    while len(received_bytes) < file_size:
        packet = client_socket.recv(1400)
        if not packet:
            break
        received_bytes.extend(packet)

    # 受信したデータをファイルとして保存（ここでは単純化してバイナリファイルとして保存）
    with open('received_file.mp4', 'wb') as f:
        f.write(received_bytes)

    # レスポンスを送信
    response = "Success!"
    client_socket.sendall(response.encode('utf-8'))

def main():
    # サーバソケットを作成し、接続待機
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    try:
        while True:
            # クライアントからの接続を待機
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # ファイルを受信
            receive_file(client_socket)

            # 接続を閉じる
            client_socket.close()
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
