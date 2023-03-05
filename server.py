import socket
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class Server:
    def __init__(self, host='localhost', port=9000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.clients = {}

    def start(self):
        self.server_socket.listen()
        print(f'Server is listening on {self.host}:{self.port}...')
        while True:
            conn, addr = self.server_socket.accept()
            print(f'New client connected: {addr}')
            secret_key = get_random_bytes(16)
            self.clients[addr] = {'conn': conn, 'key': secret_key}
            Thread(target=self.handle_client, args=(conn, secret_key,)).start()

    def handle_client(self, conn, secret_key):
        try:
            conn.send(secret_key)
            while True:
                ciphertext = conn.recv(1024)
                if not ciphertext:
                    break
                message = self.decrypt_message(secret_key, ciphertext)
                print(f'Received message from {conn.getpeername()}: {message}')
                for client_addr, client_data in self.clients.items():
                    if client_data['conn'] != conn:
                        client_data['conn'].send(self.encrypt_message(client_data['key'], message))
        except Exception as e:
            print(f'Error handling client {conn.getpeername()}: {e}')
        finally:
            conn.close()
            del self.clients[conn.getpeername()]

    def encrypt_message(self, key, message):
        cipher = AES.new(key, AES.MODE_CTR)
        ciphertext = cipher.encrypt(message.encode())
        return ciphertext

    def decrypt_message(self, key, ciphertext):
        cipher = AES.new(key, AES.MODE_CTR)
        message = cipher.decrypt(ciphertext).decode()
        return message

if __name__ == '__main__':
    Server().start()
