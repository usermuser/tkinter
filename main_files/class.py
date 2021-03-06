#!/usr/bin/python3
import sys
import socketserver
from tkinter import Tk, Canvas, Frame, BOTH, W, Button

sys.path.append("/usr/bin/python3")

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()
        print ("Клиент {} сообщает: {}".format(self.client_address[0], self.data))

        x = random.randint(1,100)

        if self.data == 'START':
            pass
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
    root.attributes('-fullscreen',True)
    # root.state('zoomed')
    root.title('Zagolovok')
    root.mainloop()  


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print('Server started')
    main()  
