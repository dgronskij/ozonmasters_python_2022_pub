import time

# Problem: how to run countup / countdown concurrently


def countup(n):
    for i in range(n):
        print('countup', i)
        time.sleep(1)


def countdown(n):
    for i in reversed(range(n)):
        print('countdown', i)
        time.sleep(1)

import threading

threading.Thread(target=countup, args=(2,)).start()
threading.Thread(target=countdown, args=(3,)).start()
