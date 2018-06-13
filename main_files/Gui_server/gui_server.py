# gui_server.py
'''

В этом варианте была задумано так:
на серваке стоит купюроприемник и нарисованы кнопки по постам.
когда нажимаешь кнопку сервак спрашивает у клиента сколько у него там денег
получает ответ и выводит на экран.
запрос происходит только в момент нажатия кнопки.

для отправки внесенных денег тож хотел кнопку сделать.

Теперь сделаем кнопку Button_6.
К ней привяжем функцию counter_6_req
В этой функции делаем запрос вида:
give_counter_6
Когда шестой клиент получит это сообщение,
он пришлет нам COUNTER_6
'''

from tkinter import *   # модуль для гуёв
import socket   # модуль для сервера
import sys   # системный модуль


# массив подключенных клиентов
arr = []
# arr = [[ip10, port0], [ip1, port1],]
conn_close_flag = False


def close_connection():
    conn_close_flag = True
    return conn_close_flag


def ask_counter_6(conn):
    msg = 'give_counter_6'
    msg.encode('utf8')
    conn.sendall(msg)
    print('requesting COUNTER_6')


def draw_window(conn = None):
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
    button6 = Button(frame2, text=u'Шестая кнопка', font=20, height=3, width=20, command=ask_counter_6(conn))
    button7 = Button(frame2, text=u'Седьмая кнопка', font=20, height=3, width=20)
    button8 = Button(frame2, text=u'Закрыть подключение', font=20, height=3, width=20,
                     command=close_connection())

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

    msg = 'end of gui function'
    return msg
    # root.mainloop()


def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):

    # the input is in bytes, so decode it
    input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)

    # MAX_BUFFER_SIZE is how big the message can be
    # this is test if it's sufficiently big
    siz = sys.getsizeof(input_from_client_bytes)
    if  siz >= MAX_BUFFER_SIZE:
        print("The length of input is probably too long: {}".format(siz))

    # decode input and strip the end of line
    input_from_client = input_from_client_bytes.decode("utf8").rstrip()
    splitted_input_from_client = input_from_client.split(';')

    # print('\n len(splitted_input_from_client) =', len(splitted_input_from_client))
    # print('splitted_input_from_client[0] =',splitted_input_from_client[0])

    # res = do_some_stuffs_with_input(input_from_client)
    # print("Result of processing {} is: {}".format(input_from_client, res))

    # if splitted_input_from_client[0] == 'start':
    #     print('"start" msg recieved')
    #     res = 'give_counter_6'
    #     vysl = res.encode("utf8")  # encode the result string
    #     conn.sendall(vysl)  # send it to client
    #     print('requesting COUNTER_6')
    #
    # if splitted_input_from_client[0] == 'COUNTER_6':
    #     print('\n recieved COUNTER_6 =', splitted_input_from_client[1])
    if conn_close_flag:
        conn.close()  # close connection
        print('Connection ' + ip + ':' + port + " ended")


def start_server():

    draw_window()

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('[*] Socket created')

    try:
        soc.bind(("127.0.0.1", 12345))
        print('[*] Socket bind complete')
    except socket.error as msg:
        import sys
        print('[Error] Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    print('[*] Socket now listening')

    # for handling task in separate jobs we need threading
    from threading import Thread

    # this will make an infinite loop needed for
    # not reseting server for every client
    while True:

        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        ip_port = [addr[0],addr[1]]

        if ip_port not in arr:
            arr.append(ip_port)

        print('[*] Accepting connection from ' + ip + ':' + port)

        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
            print('[*] Started client_thread')
        except:
            print("Terible error!")
            import traceback
            traceback.print_exc()

    soc.close()


start_server()
