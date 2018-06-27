import time

num = 100
time1 = ''
while True:
    curtime = time.strftime('%H:%M:%S')
    if curtime != time1:
        time1 = curtime
        num -= 1
        print(time1)
        print(num)
        time.sleep(0.5)