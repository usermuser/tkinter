#!/usr/bin/python3
import sys
import socketserver
from tkinter import Tk, Canvas, Frame, BOTH, W, Button

'''
На стороне сервера будет окно, в котором будем отображать посылаемые
данные и окно полученных данных.
'''

sys.path.append("/usr/bin/python3")

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()
        print ("Клиент {} сообщает: {}".format(self.client_address[0], self.data))

        if self.data == 'START': #если клиент отправил START
            print(self.data)
            self.request.sendall(bytes('WAITING', 'utf-8')) # мы ему шлем WAITING

            while True:
                self.data = self.request.recv(1024).decode()
                resp = self.data.split(';')
                if resp[0] == 'NUM':
                    num = int(resp[1])
                    print(num)
                    
        else:
            print('Неизвестный запрос от клиента')

            
class Example(Frame):
  
    def __init__(self):
        super().__init__()
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("zagolovok")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_text(20, 30, anchor=W, font="Arial",
            text="Most relationships seem so transitory")
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        quit_btn=Button(self,text='Quit',
            font=20,height=3,width=20, command=self.client_exit)
        button1=Button(self,text='button1',
            font=20,height=3,width=20)

        quit_btn.pack(pady=40,padx=60)
        #button1.pack(fill=BOTH, expand=1) # растянуть
        button1.pack(pady=80,padx=200)
        canvas.pack(fill=BOTH, expand=1)

    def client_exit(self):
            exit()

def main():
  
    root = Tk()
    ex = Example()
    # root.overrideredirect(True)
    root.overrideredirect(False)
#    root.attributes('-fullscreen',True) #enable fullscreen
    # root.state('zoomed')
    root.title('Zagolovok')
    print('before mainloop')
    root.mainloop()
    print('after mainloop ')


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print('Server started')
    main()  
