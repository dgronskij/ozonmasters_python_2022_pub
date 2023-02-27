import time

# Problem: how to run countup / countdown concurrently
# How to do that without threading?

from collections import deque


def countup(n, current=0):
    if current <= n:
        print('countup', current)
        time.sleep(1)
        s.call_soon(lambda:countup(n, current + 1))
    #  for i in range(n):
    #      print('countup', i)
    #      time.sleep(1)


def countdown(n):
    if n < 0:
        return
    print('countdown', n)
    time.sleep(1)
    s.call_soon(lambda: countdown(n - 1))
    #  for i in reversed(range(n)):
    #      print('countdown', i)
    #      time.sleep(1)


class Scheduler:
    def __init__(self):
        self._ready_to_run = deque()

    def call_soon(self, func):
        self._ready_to_run.append(func)

    def run(self):
        while self._ready_to_run:
            func = self._ready_to_run.popleft()
            func()

s = Scheduler()
s.call_soon(lambda: countup(3))
s.call_soon(lambda: countdown(4))
s.run()

