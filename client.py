import socket
from threading import Thread
from Crypto.Cipher import AES

class Client:
    def __init__(self, host='localhost', port=9000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.key = None

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        self.key = self.client_socket.recv(16)

    def start(self):
        Thread(target=self.receive_messages).start()
        while True:
            message = input('> ')
            if not message:
                break
            self.send_message(message)

    def receive_messages(self):
        while True:
            ciphertext = self.client_socket.recv(1024)
            if not ciphertext:
                break
            message = self.decrypt_message(self.key, ciphertext)
            print(message)

    def send_message(self, message):
        ciphertext = self.encrypt_message(self.key, message)
        self.client_socket.send(ciphertext)

    def encrypt_message(self, key, message):
        cipher = AES.new(key, AES.MODE_CTR)
        ciphertext = cipher.encrypt(message.encode())
        return ciphertext

    def decrypt_message(self, key, ciphertext):
        cipher = AES.new(key, AES.MODE_CTR)
        message = cipher.decrypt(ciphertext).decode()
        return message

if __name__ == '__main__':
    client = Client()
    client.connect()
    client.start()
``
