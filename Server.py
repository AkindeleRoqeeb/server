import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connection with", addr, name)

    c.send(bytes('Welcome to Life you all', 'utf-8'))

    c.close()