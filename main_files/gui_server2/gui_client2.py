# gui_client2.py

# Дентерминал, который опрашивает серваки раз в секунду
# При этом у него зупущен гуи

import socket, sys, time
from tkinter import *

HOST = 'localhost'
PORT = 9999


def get_counter(request):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
    except:
        print('Ошибка подключения к серверу')
        sys.exit(13)

    try:
        request = request
        print('type(request) = ', type(request), '\nrequest =', request)
        sock.send(bytes(request, 'utf-8'))
        recieved = sock.recv(1024).decode()
        print(recieved)
    except:
        print('Ошибка отправки данных серверу!')
        sock.close()
        sys.exit(14)

    sock.close()


def draw_window():
    root = Tk()
    root.title('GUI SERVER')

    # Готовим два фрейма для кнопок
    frame1 = Frame(root, bd=5, bg='green', relief=RAISED, )
    frame2 = Frame(root, bg='red', bd=5, relief=RAISED, )

    # Готовим кнопки
    button1 = Button(frame1, text=u'Первая кнопка', font=20, height=3, width=20)
    button2 = Button(frame1, text=u'Вторая кнопка', font=20, height=3, width=20)
    button3 = Button(frame1, text=u'Третья кнопка', font=20, height=3, width=20)
    button4 = Button(frame1, text=u'Четвертая кнопка', font=20, height=3, width=20)
    button5 = Button(frame2, text=u'Пятая кнопка', font=20, height=3, width=20)
    button6 = Button(frame2, text=u'Шестая кнопка', font=20, height=3, width=20, command=get_counter('GET_COUNTER_6'))
    button7 = Button(frame2, text=u'Седьмая кнопка', font=20, height=3, width=20)
    button8 = Button(frame2, text=u'Восьмая кнопка', font=20, height=3, width=20)

    # Рисуем фреймы
    frame1.pack(side=LEFT)
    frame2.pack(side=RIGHT)

    # Рисуем кнопки
    button1.pack(pady=40, padx=60)
    button2.pack(pady=40, padx=60)
    button3.pack(pady=40, padx=60)
    button4.pack(pady=40, padx=60)
    button5.pack(pady=40, padx=60)
    button6.pack(pady=40, padx=60)
    button7.pack(pady=40, padx=60)
    button8.pack(pady=40, padx=60)

    # Пишем текст
    text1 = Canvas(frame2)
    text1.create_text(20, 130, anchor=W, font="Purisa",
            text="Who doesn't long for someone to hold")
    text1.pack()

    root.mainloop()


draw_window()

# c = 0
# while True:
#
#     print(time.clock())
#     time.sleep(1)
#     c += 1
#
#     if c == 10:
#         break