import socket
import sys

HOST = 'localhost'
PORT = 9999

print('Клиент игры "Виселица"')
print('Подключаемся к {}:{}'.format(HOST, PORT))

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
except:
    print('Ошибка подключения к серверу')
    sys.exit(13)

try:
    sock.sendall(bytes('START', 'utf-8'))
    recieved = sock.recv(1024).decode()
except:
    print('Ошибка отправки данных серверу!')
    sock.close()
    sys.exit(14)

sock.close()
