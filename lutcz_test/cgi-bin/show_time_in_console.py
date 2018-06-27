import time

time1 = ''
while True:
    curtime = time.strftime('%H:%M:%S')
    if curtime != time1:
        time1 = curtime
        print(time1)
        time.sleep(0.2)