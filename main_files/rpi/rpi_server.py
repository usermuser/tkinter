# gui_server2.py
# Во втором варианте малина с денежным терминалом это клиент.
# Все малины на постах это сокет серверы.
#
# На малине с дентерминалом происходит опрос постовых малин каждую секунду,
# сколько у них денег.
# эта информация видна в окне дентерминала, для каждого поста.
# Сделаю одно окно.
# Когд чел вносит деньги он видит свою сумму на экране, нажав на кнопку с нужным
# постом, он тем самым отправит деньги.
# Для надежности можно сделать что бы чел зажал кнопку, или нажал два раза.

import socket, sys, time
from tkinter import *

c3=0

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
    print('[*] Recieved from client =', input_from_client)
    # splitted_input_from_client = input_from_client.split(';')

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
    # if input_from_client[0] == 'GET_COUNTER_6':
    #      print('input_from_client =', input_from_client)
    #     # print('\n recieved COUNTER_6 =', splitted_input_from_client[1])
    # conn.close()  # close connection

    if input_from_client == 'GET_COUNTER_3':
        global c3
        c3 += 1
        print('[*] Recieved GET_COUNTER_6 request')
        cur_time = time.strftime(str(c3))
        response = cur_time.encode('utf8')
        conn.send(response)
        print('[*] Sended response =', response)
        conn.close()


    if input_from_client == 'GET_COUNTER_6':
        print('[*] Recieved GET_COUNTER_6 request')
        cur_time = time.strftime('%H:%M:%S')
        response = cur_time.encode('utf8')
        conn.send(response)
        print('[*] Sended response =', response)
        conn.close()
    print('[*] Connection ' + ip + ':' + port + " ended")


def start_server():

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('[*] Socket created')

    try:
        soc.bind(('0.0.0.0', 9999))
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
        print('[*] Accepting connection from ' + ip + ':' + port)

        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
            print('\n[*] Started client_thread')
        except:
            print("Terible error!")
            import traceback
            traceback.print_exc()

    soc.close()

start_server()