# from tkinter import *
import socket

# root = Tk()

# Пока у клиента не будет кнопок
# клиент все время подключен к серверу и ждет от него сообщений,
# изначальо наш счетчик COUNTER_6 = 0
# сервер ВСЕГДА перед тем как прислать нам число, спросит у нас чему равен COUNTER_6
# мы это поймем когда он пришлет нам give_counter_6
# и мы запустить функцию "send_counter_6"
# когда сервер пришлет нам число, мы его прибавим к COUNTER_6

COUNTER_6 = 0

# клиент в самом начала шлет серваку команду старт
def send_start():

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("localhost", 12345))
    soc.send(('start').encode('utf8'))

    msg_from_serv_bytes = soc.recv(4096) # получили 4096 байт от сервера
    msg_from_serv = msg_from_serv_bytes.decode("utf8") # декодировали полученные данные

    if msg_from_serv.data == 'give_counter_6':
        print('msg_from_serv.data =', msg_from_serv)
        soc.send((COUNTER_6).encode('utf8'))
        print('COUNTER_6 sended')

def send_num(): # старая функция, на ее основе сделаю новую
    import socket

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("localhost", 12345))

    # clients_input = input("What you want to proceed my dear client?\n")
    clients_input = '100'
    soc.send(clients_input.encode("utf8"))  # we must encode the string to bytes
    result_bytes = soc.recv(4096)  # the number means how the response can be in bytes
    result_string = result_bytes.decode("utf8")  # the return will be in bytes, so decode

    print("Result from server is {}".format(result_string))

send_start()

# b = Button(root, text="OK", command=callback) # старая кнопка
# b.pack()

# b2 = Button(root, text='send 100', command=send_num) # старая кнопка
# b2.pack()

# mainloop()
