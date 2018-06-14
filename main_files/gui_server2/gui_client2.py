# gui_client2.py

# Дентерминал, который опрашивает серваки раз в секунду
# При этом у него зупущен гуи

#https://stackoverflow.com/questions/5048082/how-to-run-a-function-in-the-background-of-tkinter?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import socket, sys, time
from tkinter import *

HOST = 'localhost'
PORT = 9999

#
# def get_counter_1():
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((HOST, PORT))
#     except:
#         print('Ошибка подключения к серверу')
#         sys.exit(13)
#
#     try:
#         request = 'GET_COUNTER_5'
#         print('type(request) = ', type(request), '\nrequest =', request)
#         sock.send(bytes(request, 'utf-8'))
#         recieved = sock.recv(1024).decode()
#         print(recieved)
#     except:
#         print('Ошибка отправки данных серверу!')
#         sock.close()
#         sys.exit(14)
#
#     sock.close()
#
#
# def get_counter_2():
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((HOST, PORT))
#     except:
#         print('Ошибка подключения к серверу')
#         sys.exit(13)
#
#     try:
#         request = 'GET_COUNTER_2'
#         print('type(request) = ', type(request), '\nrequest =', request)
#         sock.send(bytes(request, 'utf-8'))
#         recieved = sock.recv(1024).decode()
#         print(recieved)
#     except:
#         print('Ошибка отправки данных серверу!')
#         sock.close()
#         sys.exit(14)
#
#     sock.close()
#
#
# def get_counter_3():
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((HOST, PORT))
#     except:
#         print('Ошибка подключения к серверу')
#         sys.exit(13)
#
#     try:
#         request = 'GET_COUNTER_3'
#         print('type(request) = ', type(request), '\nrequest =', request)
#         sock.send(bytes(request, 'utf-8'))
#         recieved = sock.recv(1024).decode()
#         print(recieved)
#     except:
#         print('Ошибка отправки данных серверу!')
#         sock.close()
#         sys.exit(14)
#
#     sock.close()
#
#
# def get_counter_4():
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((HOST, PORT))
#     except:
#         print('Ошибка подключения к серверу')
#         sys.exit(13)
#
#     try:
#         request = 'GET_COUNTER_4'
#         print('type(request) = ', type(request), '\nrequest =', request)
#         sock.send(bytes(request, 'utf-8'))
#         recieved = sock.recv(1024).decode()
#         print(recieved)
#     except:
#         print('Ошибка отправки данных серверу!')
#         sock.close()
#         sys.exit(14)
#
#     sock.close()
#
#
# def get_counter_5():
#         try:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             sock.connect((HOST, PORT))
#         except:
#             print('Ошибка подключения к серверу')
#             sys.exit(13)
#
#         try:
#             request = 'GET_COUNTER_5'
#             print('type(request) = ', type(request), '\nrequest =', request)
#             sock.send(bytes(request, 'utf-8'))
#             recieved = sock.recv(1024).decode()
#             print(recieved)
#         except:
#             print('Ошибка отправки данных серверу!')
#             sock.close()
#             sys.exit(14)
#
#         sock.close()
#
#
#
#
#
# def get_counter_7():
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((HOST, PORT))
#     except:
#         print('Ошибка подключения к серверу')
#         sys.exit(13)
#
#     try:
#         request = 'GET_COUNTER_7'
#         print('type(request) = ', type(request), '\nrequest =', request)
#         sock.send(bytes(request, 'utf-8'))
#         recieved = sock.recv(1024).decode()
#         print(recieved)
#     except:
#         print('Ошибка отправки данных серверу!')
#         sock.close()
#         sys.exit(14)
#
#     sock.close()
#
#
# def get_counter_8():
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect((HOST, PORT))
#     except:
#         print('Ошибка подключения к серверу')
#         sys.exit(13)
#
#     try:
#         request = 'GET_COUNTER_8'
#         print('type(request) = ', type(request), '\nrequest =', request)
#         sock.send(bytes(request, 'utf-8'))
#         recieved = sock.recv(1024).decode()
#         print(recieved)
#     except:
#         print('Ошибка отправки данных серверу!')
#         sock.close()
#         sys.exit(14)
#
#     sock.close()

time1 = ''

def draw_window():

    def callback():
        print('click!')

    def get_counter_3():

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
        except:
            print('Ошибка подключения к серверу')
            sys.exit(13)

        try:
            request = 'GET_COUNTER_3'
            # print('type(request) = ', type(request), '\nrequest =', request)
            sock.send(bytes(request, 'utf-8'))
            recieved = sock.recv(4096).decode()
            return recieved
            # print('recieved =', recieved)
        except:
            print('Ошибка отправки данных серверу!')
            sock.close()
            sys.exit(14)

        sock.close()

    def get_counter_6():

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
        except:
            print('Ошибка подключения к серверу')
            sys.exit(13)

        try:
            request = 'GET_COUNTER_6'
            # print('type(request) = ', type(request), '\nrequest =', request)
            sock.send(bytes(request, 'utf-8'))
            recieved = sock.recv(4096).decode()
            return recieved
            # print('recieved =', recieved)
        except:
            print('Ошибка отправки данных серверу!')
            sock.close()
            sys.exit(14)

        sock.close()


    root = Tk()
    root.title('GUI SERVER')

    # Готовим два фрейма для кнопок
    frame1 = Frame(root, bd=5, bg='green', relief=RAISED, )
    frame2 = Frame(root, bg='red', bd=5, relief=RAISED, )

    # Готовим кнопки
    # button1 = Button(frame1, text=u'Первая кнопка', font=20, height=3, width=20)
    # button2 = Button(frame1, text=u'Вторая кнопка', font=20, height=3, width=20)
    button3 = Button(frame1, text=u'Третья кнопка', font=20, height=3, width=20, command=get_counter_3)
    button4 = Button(frame1, text=u'Четвертая кнопка', font=20, height=3, width=20)
    button5 = Button(frame2, text=u'Пятая кнопка', font=20, height=3, width=20, command=callback)
    button6 = Button(frame2, text=u'Шестая кнопка', font=20, height=3, width=20, command=get_counter_6)
    # button6.bind('<Button-1>', get_counter(request='GET_COUNTER_6'))
    # button7 = Button(frame2, text=u'Седьмая кнопка', font=20, height=3, width=20)
    # button8 = Button(frame2, text=u'Восьмая кнопка', font=20, height=3, width=20)

    # Рисуем фреймы
    frame1.pack(side=LEFT)
    frame2.pack(side=RIGHT)

    # Рисуем кнопки
    # button1.pack(pady=40, padx=60)
    # button2.pack(pady=40, padx=60)
    button3.pack(pady=5, padx=5)
    button4.pack(pady=5, padx=5)
    button5.pack(pady=5, padx=5)

    button6.pack(pady=5, padx=5)

    clock = Label(frame2, font=('times', 20, 'bold'), bg='green')
    clock.pack(pady=5, padx=5)

    label_3=Label(frame1, font=('times', 20, 'bold'), bg='green')
    label_3.pack(pady=5, padx=5)

    label_6=Label(frame2, font=('times', 20, 'bold'), bg='red')
    label_6.pack(pady=5, padx=5)
    # button7.pack(pady=5, padx=5)
    # button8.pack(pady=5, padx=5)

    # Пишем текст
    # text1 = Canvas(frame2)
    # text1.create_text(20, 130, anchor=W, font="Purisa",
    #         text="Who doesn't long for someone to hold")
    # text1.pack()

    # root.after(1000, get_counter_6)  # (time_delay, method_to_execute)

    time1 = ''
    def tick():
        global time1
        # get the current local time from the PC
        time2 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(2000, tick)
        label_3.config(text=get_counter_3())
        label_6.config(text=get_counter_6())

    tick()
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