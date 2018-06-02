from tkinter import Tk, Canvas, Frame, BOTH, W, Button

class Example(Frame):
  
    def __init__(self):
        super().__init__()
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("zagolovok")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_text(20, 30, anchor=W, font="Purisa",
            text="Most relationships seem so transitory")
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        button1=Button(self,text=u'Первая кнопка',
            font=20,height=3,width=20, command=self.client_exit)

        # button1.pack(fill=BOTH, expand=1)
        button1.pack(pady=40,padx=60)
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
    root.title(u'Заголовок НАХ')
    root.mainloop()  


if __name__ == '__main__':
    main()  
