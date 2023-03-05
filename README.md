Multi-User Secure Chatroom
This is a multi-user secure chatroom implemented in Python 3. It uses the Socket module to create a TCP server that can handle multiple client connections, and the PyCrypto library to encrypt and decrypt messages using the AES cipher in counter mode (CTR).

The chatroom is secure because each client connection is encrypted using a randomly generated secret key, which is sent to the client at the beginning of the connection. The server uses this key to encrypt the messages sent by the client and decrypt the messages sent by other clients. This ensures that only clients with the correct key can read the messages, and that the messages cannot be intercepted or tampered with by third parties.

The chatroom has a simple command-line interface, where users can type messages that are broadcasted to all other users in real-time. Users can also leave the chatroom by simply typing an empty message.

To use the chatroom, simply clone the repository, run the server script (server.py) on a machine accessible by all users, and run the client script (client.py) on each user's machine. 

The client script will connect to the server and prompt the user to enter a username. Once connected, the user can type messages that will be encrypted and sent to the server, which will then broadcast them to all other users. The user can also receive messages from other users, which will be decrypted and displayed on the console.


Requirements
Python 3.x

PyCrypto (for encryption)



Limitations

The chatroom is implemented using a simple TCP server, which may not be suitable for very large numbers of users or very high traffic. For such scenarios, a more scalable solution such as a message queue or a websockets server should be used.
The chatroom does not have any authentication or authorization mechanisms, so anyone can connect and join the conversation. To add such features, a user database and login system would need to be implemented.
The chatroom does not persist messages, so once a user leaves the chatroom, they will not be able to see any messages sent while they were away. To add persistence, a database or file system could be used to store the messages.

