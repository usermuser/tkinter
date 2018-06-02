from tkinter import *

root=Tk()
#root.attributes('-fullscreen')
#root.geometry(widthxheight+x+y)
#root.geometry('700x600+300+200')
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
root.state('zoomed')
root.title(u'Заголовок НАХ')
#root.resizable(True, False) #(horizontally, vertically)

# У нас будет два фрейма, зеленый и красный
# frame3=Frame(root,bd=20,bg,height,width,borderwidth,relief)
frame1=Frame(root,
             bd=5,
             bg='green',
             relief=RAISED,)

frame2=Frame(root,
             bg='red',
             bd=5,
             relief=RAISED,)

#Надписи на кнопках
button1=Button(frame1,text=u'Первая кнопка',font=20,height=3,width=20)
button2=Button(frame1,text=u'Вторая кнопка',font=20,height=3,width=20)
button3=Button(frame1,text=u'Третья кнопка',font=20,height=3,width=20)
button4=Button(frame1,text=u'Четвертая кнопка',font=20,height=3,width=20)
button5=Button(frame2,text=u'Пятая кнопка',font=20,height=3,width=20)
button6=Button(frame2,text=u'Шестая кнопка',font=20,height=3,width=20)
button7=Button(frame2,text=u'Седьмая кнопка',font=20,height=3,width=20)
button8=Button(frame2,text=u'Восьмая кнопка',font=20,height=3,width=20)

#frame3.pack(side=RIGHT, padx=5, pady=5, expand=True)
frame1.pack(side=LEFT)
frame2.pack(side=RIGHT)

button1.pack(pady=40,padx=60)
button2.pack(pady=40,padx=60)
button3.pack(pady=40,padx=60)
button4.pack(pady=40,padx=60)
button5.pack(pady=40,padx=60)
button6.pack(pady=40,padx=60)
button7.pack(pady=40,padx=60)
button8.pack(pady=40,padx=60)
root.mainloop()
