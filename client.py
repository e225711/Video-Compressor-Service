import socket
import os

# サーバのIPアドレスとポート番号
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 9001

def send_file(file_path, server_socket):
    # ファイルのバイト数を取得
    file_size = os.path.getsize(file_path)

    # ファイルのバイト数をサーバに送信
    server_socket.sendall(str(file_size).encode('utf-8'))

    # ファイルを開いてサーバに送信
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1400)
            if not data:
                break
            server_socket.sendall(data)

    # サーバからの応答を受信
    response = server_socket.recv(16)
    print("Server response:", response.decode('utf-8'))

def main():
    # クライアントソケットを作成し、サーバに接続
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")

    try:
        # アップロードするファイルを指定
        file_path = '/Users/maimukohagura/Downloads/宮崎駿2のコピー.mp4'  # 送信するmp4ファイルのパスを指定してください

        # ファイルをサーバに送信
        send_file(file_path, client_socket)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
