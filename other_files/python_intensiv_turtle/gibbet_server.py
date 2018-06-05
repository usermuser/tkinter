import random
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()
        print ("Клиент {} сообщает: {}".format(self.client_address[0], self.data))

        x = random.randint(1,100)

        if self.data == 'START':
            pass
        else:
            print('Неизвестный запрос от клиента')

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print('Сервер игры "Виселица" запущен')

    server.serve_forever()
